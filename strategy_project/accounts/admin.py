from django.contrib import admin
from django.contrib.auth import get_user_model
from strategy_pages.models import ArticleModel
from new_chat.models import Room,MessageManager,Message

# Register your models here.

admin.site.register(get_user_model())
admin.site.register(ArticleModel)
admin.site.register(Room)
# admin.site.register(MessageManager)
# admin.site.register(Message)