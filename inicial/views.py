from django.shortcuts import render

def index(request):
    return render(request, 'inicial/index.html')
def contato(request):
    return render(request, 'inicial/contato.html')
def ranking(request):
    return render(request, 'inicial/ranking.html')