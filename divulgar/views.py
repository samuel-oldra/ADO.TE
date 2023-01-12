from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Pet, Raca, Tag


@login_required
def all_pets(request):
    if request.method == "GET":
        pets = Pet.objects.all()
        return render(request, 'dashboard.html', {'pets': pets})

@login_required
def novo_pet(request):
    tags = Tag.objects.all()
    racas = Raca.objects.all()
    return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})
