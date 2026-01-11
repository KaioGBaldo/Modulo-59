from django.urls import path
from .views import minha_view

urlpatterns = [
    path('minha-tela/', minha_view, name='minha_view'),
]
