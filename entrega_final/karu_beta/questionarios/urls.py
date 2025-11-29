'''from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questionario/', views.questionario, name='questionario'),
    path('alertas/', views.alertas, name='alertas'),
    path('dashboard_gestao/', views.dashboard_gestao, name='dashboard_gestao'),
    path('questionario_lista/', views.questionario_lista, name='questionario_lista'),
    path('questionario_responder/<int:pk>/', views.questionario_responder, name='questionario_responder'),

    # --- ALERTAS ---
    path('listar_alertas/', views.listar_alertas, name='listar_alertas'),

    # --- ACOMPANHAMENTOS ---
    path('acompanhamentos/', views.acompanhamentos_lista, name='acompanhamentos_lista'),
    path('acompanhamentos/novo/', views.acompanhamento_novo, name='acompanhamento_novo'),
    path('acompanhamentos/<int:pk>/editar/', views.acompanhamento_editar, name='editar_acompanhamento'),
    path('acompanhamentos/<int:pk>/deletar/', views.acompanhamento_deletar, name='deletar_acompanhamento'),
]'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questionario/', views.questionario, name='questionario'),
    path('alertas/', views.alertas, name='alertas'),
    path('dashboard_gestao/', views.dashboard_gestao, name='dashboard_gestao'),
    path('questionario_lista/', views.questionario_lista, name='questionario_lista'),
    path('questionario_responder/<int:pk>/', views.questionario_responder, name='questionario_responder'),
    path('acompanhamentos/', views.acompanhamentos, name='acompanhamentos'),
    path('listar_alertas/', views.listar_alertas, name='listar_alertas'),
]


