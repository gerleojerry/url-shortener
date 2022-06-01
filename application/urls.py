from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage , name='homepage'),
    path('generate/', views.generate, name = 'generate'),
    path('<str:pk>/', views.load, name = 'load')
]
