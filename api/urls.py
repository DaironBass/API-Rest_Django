'''
Este código es un ejemplo de cómo se pueden configurar las
URL en Django para trabajar con vistas basadas en conjuntos (ViewSets) 
en Django REST Framework (DRF) utilizando enrutadores (routers). '''

from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()#Se crea un objeto router utilizando routers.DefaultRouter(). Este enrutador proporciona automáticamente las URL necesarias para admitir las operaciones CRUD en los ViewSets.
router.register(r'programmers', views.ProgrammerViewSet)#Se registra el ProgrammerViewSet en el enrutador utilizando router.register(r'programmers', views.ProgrammerViewSet). Esto significa que las URL generadas por el enrutador estarán asociadas a las operaciones CRUD definidas en ProgrammerViewSet para el modelo Programmer.
                                                       #'programmers' indica que sera parte de las rutas que se crean y se asocian a las vistas, el endpoint base   

'''urlpatterns es una lista de patrones de URL de Django. 
Se utiliza path('', include(router.urls)) para incluir las 
URL generadas por el enrutador en el patrón de URL principal.
Esto significa que todas las URL generadas por el enrutador 
se agregarán a la ruta principal.'''

urlpatterns = [
    path('', include(router.urls))
]

'''Se codifica como include(router.urls) ya que las urls anteriormente creadas y relacionadas con las vistas
en el enrutador solo quedan disponiobles en esa funcion urls de ese enrutador'''

'''En resumen, este código configura las URL para el manejo 
de las operaciones CRUD en los objetos Programmer utilizando 
un ViewSet y un enrutador (Ambos se relacionan -> URL con las vistas para poder que sepa donde ir y ejecutar las vistas) 
en Django REST Framework. Las URL generadas incluirán rutas como programmers/, que se asociarán 
a las operaciones CRUD definidas en ProgrammerViewSet.'''
