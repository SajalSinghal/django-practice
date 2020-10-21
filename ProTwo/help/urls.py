from django.conf.urls import url
from django.urls import path
from help import views

urlpatterns = [
    url(r'^$', views.help, name='help')
]
