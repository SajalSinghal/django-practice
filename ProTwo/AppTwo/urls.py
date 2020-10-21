from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    # url(r'^$', views.user, name='user'),
    url(r'^$', views.new_user, name='new_user')
]
