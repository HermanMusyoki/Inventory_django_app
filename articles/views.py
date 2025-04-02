from django.shortcuts import render
from articles.models import Article


context = {
    "object" : None,
}

# Create your views here.
def article_deal_view(request, id):
    return render(request, "article/detail.html" , context= context)