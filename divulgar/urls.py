from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.all_pets, name="dashboard"),
    path('novo_pet/', views.novo_pet, name="novo_pet"),
]
