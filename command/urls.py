from django.urls import path
from . import views

app_name = 'command'
urlpatterns = [
    path('', views.commands_index, name='CommandsIndex'),
    path('list/', views.commands_list, name='CommandsList')
]
