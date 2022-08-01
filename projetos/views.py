from django.shortcuts import render
from projetos.models import Projeto

# Create your views here.



def view_all_projects(request):
    print("index")
    # return HttpResponse("Teste index")
    projetos = Projeto.objects.all()

    return render(request, 'projetos/index.html', context = {'projetos' : projetos})

def project_detail(request, pk):
    print("index")
    # return HttpResponse("Teste index")
    projeto = Projeto.objects.get(pk = pk)

    return render(request, 'projetos/detalhes.html', context = {'projeto' : projeto})