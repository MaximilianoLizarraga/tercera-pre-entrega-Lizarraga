from django.shortcuts import render
from django.http import HttpResponse
from nueva_entrega.models import Libro, Autor, Genero
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


def index(request):
     return render(request, "nueva_entrega/base.html") #verificar

   
class LibroCreate(CreateView):
    model = Libro
    success_url = reverse_lazy("libro-list")
    fields = '__all__'

class LibroList(ListView):
    model = Libro

    def get_queryset(self):

        criterio = self.request.GET.get('criterio')

        if criterio:
            book = Libro.objects.filter(titulo__icontains=criterio)
        else:
            book = Libro.objects.all()

        return book

class AutorCreate(CreateView):
    model = Autor
    success_url = reverse_lazy("autor-list")
    fields = '__all__'

class AutorList(ListView):
    model = Autor

    def get_queryset(self):

        criterio = self.request.GET.get('criterio')

        if criterio:
            book = Autor.objects.filter(nombre__icontains=criterio)
        else:
            book = Autor.objects.all()

        return book
    


class GeneroCreate(CreateView):
    model = Genero
    success_url = reverse_lazy("genero-list")
    fields = '__all__'

class GeneroList(ListView):
    model = Genero

    def get_queryset(self):

        criterio = self.request.GET.get('criterio')

        if criterio:
            book = Genero.objects.filter(genero__icontains=criterio)
        else:
            book = Genero.objects.all()

        return book
