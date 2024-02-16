from django.urls import path
from . import views

urlpatterns = [
    path ('',views.Strategy.as_view(), name='strategy'),
    path ('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path ('create/' , views.Create.as_view(), name='create'),
    path ('delete/<int:pk>', views.Delete.as_view(), name='delete'),
    path ('update/<int:pk>', views.Update.as_view(), name='update'),
]
# fanction + f2 で名前の一括変更可能
# command + クリックで定義元へジャンプ可能
