
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('departamento/',include('apps.departamento.urls')),
    path('empresa/',include('apps.empresas.urls')),
    path('funcionario/',include('apps.funcionarios.urls')),
    path('registro-ponto/',include('apps.registro_ponto.urls')),

]
