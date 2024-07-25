from .views import Homepage, Login
from django.urls import path
from django.contrib.auth import views 


app_name = 'sangue'
urlpatterns=[
    path('',Homepage.as_view(), name='homepage'), 
    path('login/',Login.as_view(), name='login'),
]