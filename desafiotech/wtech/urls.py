from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('registrar/', views.registrar, name='registrar'),
    path ('tela/', views.tela, name='tela'),
    path ('export_csv', views.export_csv, name='export_csv'),
]
