from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'index', views.index, name='index'),
   
    # ex: /polls/5/results/
   
]