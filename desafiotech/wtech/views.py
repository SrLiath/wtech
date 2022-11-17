from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import conta
import csv

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        
        auth = authenticate(username=username, password=senha)
        if auth:
            login_django(request, auth)
            return redirect(tela)
        else:
            return HttpResponse('login ou senha invalido')
    
def registrar(request):
    if request.method == "GET":
        return render(request,'cadastrar.html')
    else:
        username = request.POST.get('login')
        senha = request.POST.get('senha')
        date = request.POST.get('date')


        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuario com este login')
        if senha == "":
            senha = User.objects.make_random_password()
        conta.objects.create(login = username, date = date, senha = senha)
        
        user = User.objects.create_user(username=username, password=senha)
        user.set_password(senha)
        user.save()
        return HttpResponse('usuario cadastrado com sucesso, sua senha é ' + senha)
       
       
@login_required(login_url='home')
def tela(request):
    conta_list = conta.objects.all()
    return render (request, 'tela.html', {'conta_list': conta_list})

def export_csv(request):
    contas = conta.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=usuarios.csv'
    writer = csv.writer(response)
    writer.writerow(['login:', 'data:', 'senha:'])
    conta_fields = contas.values_list('login', 'date', 'senha')
    for contas in conta_fields:
        writer.writerow(contas)
    return response