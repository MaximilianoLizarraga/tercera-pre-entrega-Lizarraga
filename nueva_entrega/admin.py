from django.contrib import admin
from nueva_entrega.models import Libro, Autor, Genero

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Genero)
