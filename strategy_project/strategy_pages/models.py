from django.db import models
from accounts.models import User

# 攻略情報記事のmodel

class ArticleModel(models.Model):
  author = models.ForeignKey( User, on_delete=models.CASCADE ) #　ユーザーが消えると記事も消える設定。 後で消えた時に「削除されたアカウント」に変える。
  title = models.CharField( max_length = 100 )
  content = models.TextField()
  display_num = models.IntegerField( null = True, blank = True, default = 0 )
  created_at = models.DateTimeField( auto_now_add = True )
  update_at = models.DateTimeField( auto_now = True )
  
  def __str__(self):
    return self.title