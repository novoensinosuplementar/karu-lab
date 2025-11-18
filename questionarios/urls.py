from django.urls import path
from . import views

urlpatterns = [
    # Página inicial (vamos criar a view depois)
    path('', views.home, name='home'),
]