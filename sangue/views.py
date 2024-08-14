from django.shortcuts import render
from django.views.generic import TemplateView, ListView 

class Homepage(TemplateView): 
    template_name = 'homepage.html'


class Cadastro(TemplateView):
    template_name = 'cadastro.html'

class Login(TemplateView):
    template_name = 'login.html'    

class Doador(TemplateView):
    template_name = 'doador.html'    

class Agenda(TemplateView):
    template_name = 'agenda.html'     

class Receptor(TemplateView):
    template_name = 'receptor.html'      