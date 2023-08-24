import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import Registro_Ponto


from  django.views.generic import View
# Create your views here.

class registrar_ponto(View):
    def post(self,*args, **kwargs):
        selecao = "registrando hora no banco"
        user = "jhonatan"
        dataHoje = str(datetime.today())
        response = json.dumps({'mensagem':'requisicao executada teste',
                               'usuario':user,
                               'dataHoje':selecao})
        return  HttpResponse(response,content_type='application/json')

