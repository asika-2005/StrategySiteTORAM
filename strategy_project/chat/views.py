from django.shortcuts import render

# Create your views here.

def chat( request ):
  # TODO: 後でimportを使って、accountsのユーザーモデル(models.py)を引っ張る。 
  return render( request, 'chat/chat.html' )
