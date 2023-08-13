
from django.contrib.auth.decorators import login_required
from  django.views.generic import  ListView,UpdateView,DeleteView,CreateView
from django.urls import  reverse_lazy
from django.shortcuts import render
from .models import Funcionario


class funcionarios_list(ListView):
    model = Funcionario

class funcionarios_edit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos','empresa']

class funcionarios_delete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class funcionarios_create(CreateView):
    model = Funcionario
    fields = ['nome','departamentos','empresa','user']
    success_url = reverse_lazy('list_funcionarios')