from django.urls import path
from . import consumers

websocket_urlpatterns = [
  path('ws/new_chat/<int:room_id>', consumers.ChatConsumer.as_asgi()),
]