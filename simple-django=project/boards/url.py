from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('',views.Boards,name='home'),
    path('boards/<int:board_id>/',views.board_topic,name='board_topic'),
    path('boards/<int:board_id>/new/',views.new_topic,name='new_topic'),
]