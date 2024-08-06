from .views import Homepage, Cadastro, Login, Doador
from django.urls import path
from django.contrib.auth import views 


app_name = 'sangue'
urlpatterns=[
    path('',Homepage.as_view(), name='homepage'), 
    path('cadastro/',Cadastro.as_view(), name='cadastro'),
    path('login/',Login.as_view(), name= 'login'),
    path('doador/',Doador.as_view(), name='doador'),
]