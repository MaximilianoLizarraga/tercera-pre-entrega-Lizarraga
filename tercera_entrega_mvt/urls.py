"""tercera_entrega_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from nueva_entrega.views import  index, LibroCreate, LibroList, AutorList, AutorCreate, GeneroList, GeneroCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('libro/list', LibroList.as_view(), name="libro-list"),
    path('libro/create', LibroCreate.as_view(), name="libro-create"),
    path('autor/list', AutorList.as_view(), name="autor-list"),
    path('autor/create', AutorCreate.as_view(), name="autor-create"),
    path('genero/list', GeneroList.as_view(), name="genero-list"),
    path('genero/create', GeneroCreate.as_view(), name="genero-create"),
    
]
