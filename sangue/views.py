from django.shortcuts import render
from django.views.generic import TemplateView

class Homepage(TemplateView): 
    template_name = 'homepage.html'


class Cadastro(TemplateView):
    template_name = 'cadastro.html'

class Login(TemplateView):
    template_name = 'login.html'    