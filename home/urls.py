from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delcity/<int:cid>', views.delcity, name='delcity')
]