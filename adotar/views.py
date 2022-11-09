from django.shortcuts import render

from divulgar.models import Pet, Raca


def listar_pets(request):
    if request.method == "GET":
        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)

        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)

        return render(
            request,
            'listar_pets.html',
            {'pets': pets, 'racas': racas, 'cidade': cidade, 'raca_filter': raca_filter}
        )
