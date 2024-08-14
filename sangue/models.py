from django.db import models
from django.contrib.auth.models import AbstractUser

#class Usuario(AbstractUser): 
 #pass


class Doador(models.Model):   
    nome = models.CharField(max_length = 150) 
    tipoSanguineo = models.CharField(max_length = 5)   
    cpf = models.CharField(max_length = 20) 
    rg = models.CharField(max_length = 20) 
    dataNascimento = models.DateField() 
    rua = models.CharField(max_length = 50) 
    bairro = models.CharField(max_length = 50)  
    cidade = models.CharField(max_length = 50)  
    email = models.CharField(max_length = 75)  

class Receptor(models.Model):   
    nome = models.CharField(max_length = 150) 
    tipoSanguineo = models.CharField(max_length = 5)   
    cpf = models.CharField(max_length = 20) 
    rg = models.CharField(max_length = 20) 
    dataNascimento = models.DateField() 
    rua = models.CharField(max_length = 50) 
    bairro = models.CharField(max_length = 50)  
    cidade = models.CharField(max_length = 50)  
    email = models.CharField(max_length = 75) 

class AgendamentoDoacao(models.Model): 
    data = models.DateField() 
    doador = models.ForeignKey('Doador', related_name = 'doador', on_delete = models.CASCADE )   
    horario = models.TimeField()  
    tipoSanguineo = models.CharField(max_length = 5) 
    quantidadeSangueML = models.IntegerField()  
  
class AgendamentoRecepcao(models.Model):
    data = models.DateField() 
    receptor = models.ForeignKey('Receptor', related_name = 'receptor', on_delete = models.CASCADE )  
    horario = models.TimeField() 
    tipoSanguineo = models.CharField(max_length = 5)
    quantidadeSangueML = models.IntegerField() 
    recepcaoRealizada = models.BooleanField(default = False)   

class DoacaoInformada(models.Model):
    doador = models.ForeignKey('Doador', related_name = 'doador_email', on_delete = models.CASCADE )   
    doacao = models.ForeignKey('AgendamentoDoacao', related_name = 'doacao_agendada', on_delete = models.CASCADE )   
    dataVencimento = models.DateField()
    descricao = models.CharField(max_length = 150) 

class RecepcaoInformada(models.Model):
    receptor = models.ForeignKey('Receptor', related_name = 'receptor_email', on_delete = models.CASCADE )   
    recepcao = models.ForeignKey('AgendamentoRecepcao', related_name = 'recepcao_agendada', on_delete = models.CASCADE )   
    dataVencimento = models.DateField()
    descricao = models.CharField(max_length = 150)    


