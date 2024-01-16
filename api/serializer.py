from rest_framework import serializers #: Importa la clase base ModelSerializer y otras funcionalidades del módulo de serializadores de Django REST Framework.
from .models import Programmer  #Importa el modelo Programmer definido en el mismo directorio (o paquete) que este archivo.

'''Define una clase llamada ProgrammerSerializer que hereda de serializers.
ModelSerializer. Al heredar de esta clase, se obtienen automáticamente algunas 
funcionalidades para la serialización y deserialización de objetos.'''

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta: #En esta clase, se especifica la configuración del serializador.
        model = Programmer #: Indica que este serializador se utilizará para el modelo 
        #fields = ('fullname', 'nickname')
        fields = '__all__' # Especifica que se deben incluir todos los campos del modelo en la serializació

        '''NOTA: La clase 'Meta' y las variables 'model', 'fields'
              son convenciones estandarizadas por django rest, en el
              caso de de fields siempre es utilizado para especificar que campos
              de un modelo se quieren seralizar''' 