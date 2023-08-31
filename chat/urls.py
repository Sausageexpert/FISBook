from django.urls import path
from . import views

urlpatterns = [
    path('<str:room>', views.room, name='room'),
    path('', views.home, name='home'),
    path('checkForRoom/', views.checkForRoom, name='checkForRoom')
]
