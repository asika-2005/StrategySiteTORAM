from django.contrib import admin
from django.contrib.auth import get_user_model
from strategy_pages.models import ArticleModel

# Register your models here.

admin.site.register(get_user_model())
admin.site.register(ArticleModel)