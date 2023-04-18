from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('adicionar_sobrevivente/', views.adicionar_sobrevivente, name='adicionar_sobrevivente'),
    path('lista_nao_infectados/', views.lista_nao_infectados, name='lista_nao_infectados'),
    path('lista_infectados/', views.lista_infectados, name='lista_infectados'),
    path('atualizar_sobrevivente/<int:sobrevivente_id>/', views.atualizar_sobrevivente, name='atualizar_sobrevivente'),
    path('dados/', views.dados, name='dados'),
    path('troca/', views.troca, name='troca'),
]


