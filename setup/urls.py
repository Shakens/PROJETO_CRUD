from django.contrib import admin
from django.urls import path
from clima.views import (
    HomeListView,
    TipoSensorCreateView,
    TipoSensorDeleteView,
    TipoSensorDetailView,
    TipoSensorListView,
    TipoSensorUpdateView,
    dashboard_view,
    temperatura_dados,
    SalaCreateView,
    SalaUpdateView,
    SalaDetailView,
    SalaDeleteView,
    SalaListView,
    ParametroCreateView,
    ParametroUpdateView,
    ParametroDetailView,
    ParametroDeleteView,
    ParametroListView,
    LeituraTemperaturaCreateView,
    LeituraTemperaturaListView,
    LeituraTemperaturaDetailView,
)

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para acessar o painel de administração do Django

    # =================== Rotas para Sensores ===================
    path("", HomeListView.as_view(), name="home"),  # Rota para a home (lista de sensores)
    path("sensor/", TipoSensorListView.as_view(), name="tipo_sensor_list"),  # Lista de sensores
    path("sensor/create/", TipoSensorCreateView.as_view(), name="tipo_sensor_create"),  # Criação de sensor
    path("sensor/update/<int:pk>/", TipoSensorUpdateView.as_view(), name="tipo_sensor_update"),  # Atualização de sensor
    path("sensor/delete/<int:pk>/", TipoSensorDeleteView.as_view(), name="tipo_sensor_delete"),  # Exclusão de sensor
    path("sensor/detail/<int:pk>/", TipoSensorDetailView.as_view(), name="tipo_sensor_detail"),  # Detalhes do sensor

    # =================== Rota do Dashboard ===================
    path("dashboard/", dashboard_view, name="dashboard"),  # Rota para o dashboard

    # =================== Rota do gráfico de temperatura ===================
    path('temperatura/dados/', temperatura_dados, name='temperatura_dados'),  # Dados de temperatura
    path('temperatura/dados/<int:sensor_id>/', temperatura_dados, name='temperatura_dados_sensor'),  # Dados de temperatura de um sensor específico

    # =================== Rotas para Salas ===================
    path("salas/", SalaListView.as_view(), name="sala_list"),  # Lista de salas
    path("salas/create/", SalaCreateView.as_view(), name="sala_create"),  # Criação de sala
    path("salas/update/<int:pk>/", SalaUpdateView.as_view(), name="sala_update"),  # Atualização de sala
    path("salas/detail/<int:pk>/", SalaDetailView.as_view(), name="sala_detail"),  # Detalhes da sala
    path("salas/delete/<int:pk>/", SalaDeleteView.as_view(), name="sala_delete"),  # Exclusão de sala

    # =================== Rotas para Parâmetros ===================
    path("parametros/", ParametroListView.as_view(), name="parametro_list"),  # Lista de parâmetros
    path("parametros/create/", ParametroCreateView.as_view(), name="parametro_create"),  # Criação de parâmetro
    path("parametros/update/<int:pk>/", ParametroUpdateView.as_view(), name="parametro_update"),  # Atualização de parâmetro
    path("parametros/detail/<int:pk>/", ParametroDetailView.as_view(), name="parametro_detail"),  # Detalhes do parâmetro
    path("parametros/delete/<int:pk>/", ParametroDeleteView.as_view(), name="parametro_delete"),  # Exclusão de parâmetro

    # =================== Rotas para Leitura de Temperatura ===================
    path('leitura-temperatura/', LeituraTemperaturaListView.as_view(), name='leitura_temperatura_list'),  # Lista de leituras de temperatura
    path('leitura-temperatura/create/', LeituraTemperaturaCreateView.as_view(), name='leitura_temperatura_create'),  # Criação de leitura de temperatura
    path('leitura-temperatura/detail/<int:pk>/', LeituraTemperaturaDetailView.as_view(), name='leitura_temperatura_detail'),  # Detalhes da leitura de temperatura
]
