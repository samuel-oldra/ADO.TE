from django.urls import path

from . import views

urlpatterns = [
    path('novo_pet/', views.novo_pet, name="novo_pet"),
]
