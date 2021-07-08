from django.urls import path
from .views import home, formulario, listadoObra,add_obra, edit_obra, borrar_obra,galeria 
urlpatterns = [
    path('', home, name="inicio_home"),
    path('formulario-contacto', formulario, name='contacto'),
    path('listado-obras', listadoObra, name='listado'),
    path('agregar-obra', add_obra, name='agregar'),
    path('editar-obra/<pk>', edit_obra, name='editar_obra'),
    path('eliminar-obra/<pk>', borrar_obra, name='borrar_obra'),
    path('galeria', galeria, name='galeria'),
    #path('detalle-obra/<pk>', detalleObra, name='detalle_obra')
]