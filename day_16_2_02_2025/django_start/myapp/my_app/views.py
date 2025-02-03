from django.shortcuts import render
from django.http import HttpResponse

from  .models import Article


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'my_app/article_list.html', {'articles': articles})



def home(request):
    return HttpResponse("To jest przykładowy tekst zwracany przez endpoint /")


