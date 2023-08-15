
from django.urls import path
from .views import  departamento_list,departamento_create,departamento_update,departamento_delete


urlpatterns = [
    path('', departamento_list.as_view(), name='list_departamento'),
    path('novo',departamento_create.as_view(),name='create_departamento'),
    path('edit/<int:pk>',departamento_update.as_view(),name='update_departamento'),
    path('delete/<int:pk>',departamento_delete.as_view(),name='delete_departamento')
]