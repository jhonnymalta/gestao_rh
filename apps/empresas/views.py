from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import Empresa


@login_required
def DeletePage(request):
    return render(request,'empresas/delete_empresa.html')


class EmpresaList(ListView):
    model = Empresa


class EmpresaCreateViewModel(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        form.save()
        success_url = reverse_lazy('list_empresa')

class EmpresaEditViewModel(UpdateView):
    model = Empresa
    fields=['nome']

    def form_valid(self, form):
        form.save()
        return HttpResponse('OK')

class EmpresaDeleteViewModel(DeleteView):
    model = Empresa
    success_url = ''