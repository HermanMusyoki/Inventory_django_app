from django.shortcuts import render
from .models import Article




# Create your views here.
def article_detail_view(request, id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
    "object" : None,
    }
    return render(request, "article/detail.html" , context= context)