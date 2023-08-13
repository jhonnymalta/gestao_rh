
from django.urls import path
from .views import  funcionarios_list,funcionarios_edit,funcionarios_delete,funcionarios_create


urlpatterns = [
    path('', funcionarios_list.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', funcionarios_edit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>', funcionarios_delete.as_view(), name='delete_funcionario'),
    path('create/', funcionarios_create.as_view(), name='create_funcionario'),



]
