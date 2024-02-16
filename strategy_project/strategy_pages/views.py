from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import ArticleModel
from django.urls import reverse_lazy

# Create your views here.

# def strategy( request ):
#   context = dict()
#   context['object_list'] = ArticleModel.objects.all()
#   return render( request , 'strategy/strategy.html' , context = context )

class Strategy(ListView):
  template_name = 'strategy_pages/strategy.html'
  model = ArticleModel

class Detail(DetailView):
  template_name = 'strategy_pages/detail.html'
  model = ArticleModel

class Create(CreateView):
  template_name = 'strategy_pages/create.html'
  model = ArticleModel
  fields = ('title', 'content', 'author')
  success_url = reverse_lazy('strategy')

class Delete(DeleteView):
  template_name = 'strategy_pages/delete.html'
  model = ArticleModel
  success_url = reverse_lazy('strategy')

class Update(UpdateView):
  template_name = 'strategy_pages/update.html'
  model = ArticleModel
  fields = ('title', 'content', 'author')
  success_url = reverse_lazy('strategy')