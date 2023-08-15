from django.shortcuts import render
from  django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import  reverse_lazy
from .models import Departamento

# Create your views here.
class departamento_list(ListView):
    model = Departamento


class departamento_create(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.save()
        return super(departamento_create,self).form_valid(form)

class departamento_update(UpdateView):
    model = Departamento
    fields = ['nome']

class departamento_delete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamento')