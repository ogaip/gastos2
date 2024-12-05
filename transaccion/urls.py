
from django.urls import path
from . import views as  transaccion_views

urlpatterns = [
    path("gastos/", transaccion_views.gastos, name="gastos"),
]
