from django.urls import path
from loja.views.AuthView import login_view, register_view

urlpatterns = [
    path("login", login_view, name='login'),
    # Adicione a linha a seguir
    path("register", register_view, name='register'),    
]