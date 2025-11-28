from django.urls import path
from . import views

urlpatterns = [
    # === DASHBOARD ===
    path('', views.dashboard, name='dashboard'),

    # === MEDICAÇÕES ===
    path('medicacoes/', views.listar_medicacoes, name='listar_medicacoes'),
    path('medicacoes/nova/', views.criar_medicacao, name='criar_medicacao'), # <--- O erro sumirá por causa dessa linha
    path('medicacoes/editar/<int:id>/', views.editar_medicacao, name='editar_medicacao'),

    # === LEMBRETES ===
    path('lembretes/', views.listar_lembretes, name='listar_lembretes'),
    path('lembretes/novo/', views.criar_lembrete, name='criar_lembrete'), # <--- E dessa aqui
    path('lembretes/editar/<int:id>/', views.editar_lembrete, name='editar_lembrete'),

    # === ESTOQUE ===
    path('estoque/', views.listar_estoque, name='listar_estoque'),
    path('estoque/novo/', views.criar_estoque, name='criar_estoque'), # <--- E dessa aqui
    path('estoque/editar/<int:id>/', views.editar_estoque, name='editar_estoque'),

    # === REGISTROS ===
    path('registros/', views.listar_registros, name='listar_registros'),
]
