
from django.urls import path
from .views import EmpresaCreateViewModel,EmpresaEditViewModel

urlpatterns = [
    path('nova/',EmpresaCreateViewModel.as_view(), name='create_empresa'),
    path('edit/',EmpresaEditViewModel.as_view(), name='edit_empresa'),

]
