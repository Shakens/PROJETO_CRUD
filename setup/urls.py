from django.contrib import admin
from django.urls import path
from clima.views import (
    HomeListView,
    
    # Tipo Sensor
    TipoSensorCreateView, TipoSensorDeleteView, TipoSensorDetailView,
    TipoSensorListView, TipoSensorUpdateView,

    # Sala
    SalaCreateView, SalaUpdateView, SalaDetailView, SalaDeleteView, SalaListView,

    # Parâmetro
    ParametroCreateView, ParametroUpdateView, ParametroDetailView,
    ParametroDeleteView, ParametroListView,

    # Pavimento
    PavimentoListView, PavimentoCreateView, PavimentoUpdateView,
    PavimentoDetailView, PavimentoDeleteView,

    # Sensor Físico
    SensorFisicoListView, SensorFisicoCreateView, SensorFisicoUpdateView,
    SensorFisicoDeleteView, SensorFisicoDetailView,

    # Sensor Lógico
    SensorLogicoListView, SensorLogicoCreateView, SensorLogicoUpdateView,
    SensorLogicoDeleteView, SensorLogicoDetailView,

    # Orientação
    OrientacaoListView, OrientacaoCreateView, OrientacaoUpdateView,
    OrientacaoDetailView, OrientacaoDeleteView,

    # Relatórios
    RelatorioFormView, render_pdf, relatorio_list,

)

urlpatterns = [
    path('admin/', admin.site.urls),

    # =================== Home ===================
    path('', HomeListView.as_view(), name='home'),

    # =================== Tipo Sensor ===================
    path('tipo-sensor/', TipoSensorListView.as_view(), name='tipo_sensor_list'),
    path('tipo-sensor/create/', TipoSensorCreateView.as_view(), name='tipo_sensor_create'),
    path('tipo-sensor/update/<int:pk>/', TipoSensorUpdateView.as_view(), name='tipo_sensor_update'),
    path('tipo-sensor/delete/<int:pk>/', TipoSensorDeleteView.as_view(), name='tipo_sensor_delete'),
    path('tipo-sensor/detail/<int:pk>/', TipoSensorDetailView.as_view(), name='tipo_sensor_detail'),

    # =================== Sala ===================
    path('salas/', SalaListView.as_view(), name='sala_list'),
    path('salas/create/', SalaCreateView.as_view(), name='sala_create'),
    path('salas/update/<int:pk>/', SalaUpdateView.as_view(), name='sala_update'),
    path('salas/detail/<int:pk>/', SalaDetailView.as_view(), name='sala_detail'),
    path('salas/delete/<int:pk>/', SalaDeleteView.as_view(), name='sala_delete'),

    # =================== Parâmetro ===================
    path('parametros/', ParametroListView.as_view(), name='parametro_list'),
    path('parametros/create/', ParametroCreateView.as_view(), name='parametro_create'),
    path('parametros/update/<int:pk>/', ParametroUpdateView.as_view(), name='parametro_update'),
    path('parametros/detail/<int:pk>/', ParametroDetailView.as_view(), name='parametro_detail'),
    path('parametros/delete/<int:pk>/', ParametroDeleteView.as_view(), name='parametro_delete'),

    # =================== Pavimento ===================
    path('pavimentos/', PavimentoListView.as_view(), name='pavimento_list'),
    path('pavimentos/create/', PavimentoCreateView.as_view(), name='pavimento_create'),
    path('pavimentos/update/<int:pk>/', PavimentoUpdateView.as_view(), name='pavimento_update'),
    path('pavimentos/detail/<int:pk>/', PavimentoDetailView.as_view(), name='pavimento_detail'),
    path('pavimentos/delete/<int:pk>/', PavimentoDeleteView.as_view(), name='pavimento_delete'),

    # =================== Sensor Físico ===================
    path('sensor-fisico/', SensorFisicoListView.as_view(), name='sensor_fisico_list'),
    path('sensor-fisico/create/', SensorFisicoCreateView.as_view(), name='sensor_fisico_create'),
    path('sensor-fisico/update/<int:pk>/', SensorFisicoUpdateView.as_view(), name='sensor_fisico_update'),
    path('sensor-fisico/delete/<int:pk>/', SensorFisicoDeleteView.as_view(), name='sensor_fisico_delete'),
    path('sensor-fisico/detail/<int:pk>/', SensorFisicoDetailView.as_view(), name='sensor_fisico_detail'),

    # =================== Sensor Lógico ===================
    path('sensor-logico/', SensorLogicoListView.as_view(), name='sensor_logico_list'),
    path('sensor-logico/create/', SensorLogicoCreateView.as_view(), name='sensor_logico_create'),
    path('sensor-logico/update/<int:pk>/', SensorLogicoUpdateView.as_view(), name='sensor_logico_update'),
    path('sensor-logico/delete/<int:pk>/', SensorLogicoDeleteView.as_view(), name='sensor_logico_delete'),
    path('sensor-logico/detail/<int:pk>/', SensorLogicoDetailView.as_view(), name='sensor_logico_detail'),

    # =================== Orientação ===================
    path('orientacao/', OrientacaoListView.as_view(), name='orientacao_list'),
    path('orientacao/create/', OrientacaoCreateView.as_view(), name='orientacao_create'),
    path('orientacao/update/<int:pk>/', OrientacaoUpdateView.as_view(), name='orientacao_update'),
    path('orientacao/detail/<int:pk>/', OrientacaoDetailView.as_view(), name='orientacao_detail'),
    path('orientacao/delete/<int:pk>/', OrientacaoDeleteView.as_view(), name='orientacao_delete'),

    # =================== Relatórios ===================
    path('relatorio/', relatorio_list, name='relatorio_list'),
    path('relatorio/filtrar/', RelatorioFormView.as_view(), name='relatorio_form'),
    path('relatorio/pdf/', render_pdf, name='relatorio_pdf'),
]