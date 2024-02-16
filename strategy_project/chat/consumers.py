import json
from channels.generic.websocket import AsyncWebsocketConsumer
import datetime
from collections import defaultdict
from accounts.models import User
#import  PySimpleGUI as sg エラー表示用のGUIインポート

import hashlib

user_messege_count = defaultdict(int)
USERNAME_SYSTEM = '*systemm*'

# ChatConsumerクラス:WebSocketから受け取ったものを処理するクラス
class ChatConsumer( AsyncWebsocketConsumer ):

  #ルーム管理
  rooms = None

  def __init__ (self, *args, **kwargs):
    super().__init__ (*args, **kwargs)
    if ChatConsumer.rooms is None:
       ChatConsumer.rooms = {}
    self.strGroupName=''
    self.strUserName=''

  @property  # 追加
  async def hashStrGroupName(self):
     hash_ = str(hashlib.sha256(self.strGroupName.encode()).hexdigest())
     print(self.strGroupName, "-> hash ->", hash_)
     return hash_
    
  async def connect(self):

   # self.strGroupName = 'chat'
   # await self.channel_layer.group_add(self.strGroupName,self.channel_name )

    await self.accept()

  async def disconnect(self, close_code ):

   # await self.channel_layer.group_discard( self.strGroupName,self.channel_name )

    await self.leave_chat()

  async def chat_message( self,data ):
    # print(data)
    data_json = {
      'message':data['message'],
      'username':data['username'],
      'datetime':data['datetime'],
    }

    await self.send( text_data=json.dumps( data_json ) )

  async def join_chat( self,strRoomName ):
    #self.strGroupName = 'chat'
    self.strGroupName = 'chat_%s' %  strRoomName

    #print('join-chat')

    await self.channel_layer.group_add( self.strGroupName, self.channel_name )
    # await self.channel_layer.group_add( self.hashStrGroupName, self.channel_name )

    room = ChatConsumer.rooms.get(self.strGroupName)
    if( room is None ):
       ChatConsumer.rooms[self.strGroupName] = {'participants_count':1}
    else:
      room['participants_count']+= 1
    strMessage = '"' + self.strUserName + '" joined. there are ' + str( ChatConsumer.rooms[self.strGroupName]['participants_count'] ) + 'participants'
    data = {
        'type': 'chat_message', # 受信処理関数名
        'message': strMessage, # メッセージ
        'username': USERNAME_SYSTEM, # ユーザー名
        'datetime': datetime.datetime.now().strftime( '%Y/%m/%d %H:%M:%S' ), # 現在時刻
    }
    await self.channel_layer.group_send( self.strGroupName, data )

  async def leave_chat( self ):
        #print(self.strGroupName,ChatConsumer.rooms)
        if( '' == self.strGroupName ):
            return
        await self.channel_layer.group_discard( self.strGroupName, self.channel_name )
        # await self.channel_layer.group_discard( self.hashStrGroupName, self.channel_name )
        ChatConsumer.rooms[self.strGroupName]['participants_count']-= 1
        strMessage = '"' + self.strUserName + '" left. tere are ' + str( ChatConsumer.rooms[self.strGroupName]['participants_count']) + 'participants'
        data = {
            'type': 'chat_message', # 受信処理関数名
            'message': strMessage, # メッセージ
            'username': USERNAME_SYSTEM, # ユーザー名
            'datetime': datetime.datetime.now().strftime( '%Y/%m/%d %H:%M:%S' ), # 現在時刻
        }
        await self.channel_layer.group_send( self.strGroupName, data )
        if ( 0 == ChatConsumer.rooms[self.strGroupName]['participants_count']):
           del ChatConsumer.rooms[self.strGroupName]
        self.strGroupName = ''

  async def receive(self, text_data):
      global user_messege_count

      text_data_json = json.loads(text_data)
      
      # 参加処理
      if 'join' == text_data_json.get('data_type'):
          self.strUserName = text_data_json['username']
          strRoomName = text_data_json['roomname']
          await self.join_chat( strRoomName )

      elif 'leave' == text_data_json.get('data_type'):
          await self.leave_chat()

      else:
         # 送信回数制限
         if user_messege_count[self.strUserName] >= 5:
            #sg.popup_error('popup_error') エラーポップアップ表示用(現在使用不可)
            return
         
         # 送信文字数制限
         strMessage = text_data_json['message']
         if len(strMessage) > 300:
            #sg.popup_error('popup_error') 同上
            return
         
         user_messege_count[self.strUserName] += 1

         data = {
            'type': 'chat_message',
            'message': strMessage,
            'username': self.strUserName,
            'datetime': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
         }

         await self.channel_layer.group_send(self.strGroupName, data)