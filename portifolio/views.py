from django.shortcuts import render

def home(request):
    print("Home")
    return render(request, 'projetos/home.html')