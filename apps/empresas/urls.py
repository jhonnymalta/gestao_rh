
from django.urls import path
from .views import EmpresaCreateViewModel,EmpresaEditViewModel,DeletePage,EmpresaList

urlpatterns = [
    path('nova/',EmpresaCreateViewModel.as_view(), name='create_empresa'),
    path('listar/',EmpresaList.as_view(), name='list_empresa'),
    path('delete/',DeletePage ,name='delete_empresa'),

]
