from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer

class ProgrammerViewSet(viewsets.ModelViewSet): #ModelViewSet es una clase proporcionada por Django REST Framework que combina las operaciones CRUD estándar (listar, crear, recuperar, actualizar y destruir) para un modelo específico.
    queryset = Programmer.objects.all() #queryset: Especifica el conjunto de consultas que se utilizará para recuperar los objetos del modelo Programmer. En este caso, se seleccionan todos los objetos del modelo.
    serializer_class = ProgrammerSerializer #serializer_class: Indica el serializador que se utilizará para convertir los objetos del modelo en datos serializados y viceversa. En este caso, se utiliza el serializador ProgrammerSerializer.


    '''NOTA Todos los nombres de las clases, estructura y  
             variables son estandrizados por django'''


