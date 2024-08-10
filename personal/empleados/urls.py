from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

path('empleados/', views.lista_empleados, name='empleados'),
    path('empleados/<int:empleado_id>/', views.detalle, name='detalle'),
    
]