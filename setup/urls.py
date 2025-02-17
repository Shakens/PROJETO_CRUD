from django.contrib import admin
from django.urls import path
from clima import views  # Certifique-se de que suas views estão importadas corretamente
from clima.views import (
    HomeListView,
    TipoSensorCreateView,
    TipoSensorDeleteView,
    TipoSensorDetailView,
    TipoSensorListView,
    TipoSensorUpdateView,
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
    PavimentoListView,  
    PavimentoCreateView,
    PavimentoUpdateView,
    PavimentoDetailView,
    PavimentoDeleteView,
    SensorFisicoListView,
    SensorFisicoCreateView,
    SensorFisicoUpdateView,
    SensorFisicoDeleteView,
    SensorFisicoDetailView,
    SensorLogicoListView,
    SensorLogicoCreateView,
    SensorLogicoUpdateView,
    SensorLogicoDeleteView,
    SensorLogicoDetailView,
    OrientacaoListView,
    OrientacaoCreateView,
    OrientacaoUpdateView,
    OrientacaoDetailView,
    OrientacaoDeleteView,
    RelatorioListView,
    RelatorioCreateView, 
    RelatorioUpdateView,
    RelatorioDetailView,
    RelatorioDeleteView,
    LeituraSensorListView,
    LeituraSensorCreateView,  # Adicionando a view para criar leitura de sensor
    LeituraCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # =================== Rotas para Sensores ===================
    path("", HomeListView.as_view(), name="home"),
    path("sensor/", TipoSensorListView.as_view(), name="tipo_sensor_list"),
    path("sensor/create/", TipoSensorCreateView.as_view(), name="tipo_sensor_create"),
    path("sensor/update/<int:pk>/", TipoSensorUpdateView.as_view(), name="tipo_sensor_update"),
    path("sensor/delete/<int:pk>/", TipoSensorDeleteView.as_view(), name="tipo_sensor_delete"),
    path("sensor/detail/<int:pk>/", TipoSensorDetailView.as_view(), name="tipo_sensor_detail"),

    # =================== Rotas para Salas ===================
    path("salas/", SalaListView.as_view(), name="sala_list"),
    path("salas/create/", SalaCreateView.as_view(), name="sala_create"),
    path("salas/update/<int:pk>/", SalaUpdateView.as_view(), name="sala_update"),
    path("salas/detail/<int:pk>/", SalaDetailView.as_view(), name="sala_detail"),
    path("salas/delete/<int:pk>/", SalaDeleteView.as_view(), name="sala_delete"),

    # =================== Rotas para Parâmetros ===================
    path("parametros/", ParametroListView.as_view(), name="parametro_list"),
    path("parametros/create/", ParametroCreateView.as_view(), name="parametro_create"),
    path("parametros/update/<int:pk>/", ParametroUpdateView.as_view(), name="parametro_update"),
    path("parametros/detail/<int:pk>/", ParametroDetailView.as_view(), name="parametro_detail"),
    path("parametros/delete/<int:pk>/", ParametroDeleteView.as_view(), name="parametro_delete"),

    # =================== Rotas para Pavimentos ===================
    path("pavimentos/", PavimentoListView.as_view(), name="pavimento_list"),
    path("pavimentos/create/", PavimentoCreateView.as_view(), name="pavimento_create"),
    path("pavimentos/update/<int:pk>/", PavimentoUpdateView.as_view(), name="pavimento_update"),
    path("pavimentos/detail/<int:pk>/", PavimentoDetailView.as_view(), name="pavimento_detail"),
    path("pavimentos/delete/<int:pk>/", PavimentoDeleteView.as_view(), name="pavimento_delete"),

    # =================== Rotas para Sensor Físico ===================
    path("sensor-fisico/", SensorFisicoListView.as_view(), name="sensor_fisico_list"),
    path("sensor_fisico/create/", SensorFisicoCreateView.as_view(), name="sensor_fisico_create"),
    path("sensor_fisico/update/<int:pk>/", SensorFisicoUpdateView.as_view(), name="sensor_fisico_update"),
    path("sensor_fisico/delete/<int:pk>/", SensorFisicoDeleteView.as_view(), name="sensor_fisico_delete"),
    path("sensor_fisico/detail/<int:pk>/", SensorFisicoDetailView.as_view(), name="sensor_fisico_detail"),

    # =================== Rotas para Sensor Lógico ===================
    path("sensor-logico/", SensorLogicoListView.as_view(), name="sensor_logico_list"),
    path("sensor-logico/create/", SensorLogicoCreateView.as_view(), name="sensor_logico_create"),
    path("sensor-logico/update/<int:pk>/", SensorLogicoUpdateView.as_view(), name="sensor_logico_update"),
    path("sensor-logico/delete/<int:pk>/", SensorLogicoDeleteView.as_view(), name="sensor_logico_delete"),
    path("sensor-logico/detail/<int:pk>/", SensorLogicoDetailView.as_view(), name="sensor_logico_detail"),

    # =================== Rotas para Orientação ===================
    path("orientacao/", OrientacaoListView.as_view(), name="orientacao_list"),
    path("orientacao/create/", OrientacaoCreateView.as_view(), name="orientacao_create"),
    path("orientacao/update/<int:pk>/", OrientacaoUpdateView.as_view(), name="orientacao_update"),
    path("orientacao/detail/<int:pk>/", OrientacaoDetailView.as_view(), name="orientacao_detail"),
    path("orientacao/delete/<int:pk>/", OrientacaoDeleteView.as_view(), name="orientacao_delete"),

    # =================== Rota do Relatório ===================
    path("relatorio/", views.RelatorioListView.as_view(), name="relatorio_list"),
    path("relatorio/create/", views.RelatorioCreateView.as_view(), name="relatorio_create"),
    path("relatorio/update/<int:pk>/", views.RelatorioUpdateView.as_view(), name="relatorio_update"),
    path("relatorio/detail/<int:pk>/", views.RelatorioDetailView.as_view(), name="relatorio_detail"),
    path("relatorio/delete/<int:pk>/", views.RelatorioDeleteView.as_view(), name="relatorio_delete"),
    path("relatorio/pdf/", views.gerar_relatorio, name="gerar_relatorio_pdf"),


    # =================== Rotas para Leitura Sensor ===================
    path("leitura-sensor/create/<int:pk>/leitura", LeituraSensorCreateView.as_view(), name="leitura_sensor_create"),  # Adicionando a rota para criação
    path("leitura_sensor/", LeituraSensorListView.as_view(), name="leitura_sensor_list"),  # Rota para listar as leituras
    #=========================Leitura================================
    path('leitura/<int:sala_id>/criar/', LeituraCreateView.as_view(), name='criar_leitura'),
]
