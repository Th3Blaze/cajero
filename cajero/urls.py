from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_view,name='index'),
    path('cajero/',views.cajero_view,name='cajero'),
    path('salir/',views.salir,name='salir'),
    path('giro/',views.giro_view,name='giro'),
    path('deposito/',views.deposito_view,name='deposito'),
    path('balance',views.balance_view,name='balance'),
]
