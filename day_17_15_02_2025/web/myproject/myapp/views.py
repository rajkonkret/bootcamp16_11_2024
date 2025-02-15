from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def home(request):
#     return HttpResponse("Witaj w mojej aplikacji Django!")

def home(request):
    return render(request, 'myapp/index.html', {"message": "Django działa!"})
