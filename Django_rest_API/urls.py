"""
URL configuration for Django_rest_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls #include_docs_urls: Es una función proporcionada por Django 
                                                            #REST Framework que genera las rutas necesarias para la documentación de la API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('docs/',include_docs_urls(title='Api Documentation')) #title y todo lo demas es de include_docs_urls
]

'''Simplemente se agrega la URL de la aplicacion a la que queremos ejecutar, 
                                            incluyendo el archivo donde se encuentran todas las URL de es aplicacion.'''

