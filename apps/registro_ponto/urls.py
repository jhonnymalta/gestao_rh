
from django.urls import path
from .views import  registrar_ponto


urlpatterns = [
    path('registrar/', registrar_ponto.as_view() , name='registrar_ponto'),

]