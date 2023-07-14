from django.db import models
from django import forms

# Create your models here.
class conta(models.Model):
    login = models.CharField(max_length=30, primary_key=True)
    date = models.DateField()
    senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.login
        return self.senha
    