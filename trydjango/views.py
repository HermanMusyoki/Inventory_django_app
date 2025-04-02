from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
import random

randomId = random.randint(1, 4)

#from database
article_obj = Article.objects.get(id=1)
article_queryset = Article.objects.all()

context = {
    "object_list" : article_queryset,
    "id" : article_obj.id,
    "title" : article_obj.title,
    "content" : article_obj.content,

}
#article_title = article_obj.title
#article_content = article_obj.content


HTML_RESPONSE = render_to_string("base.html",context= context)
#HTML_RESPONSE = """
#<h1> {id} {title}</h1>
#<h4>{content}</h4>
#""".format(**context)

def home(request):
    return HttpResponse(HTML_RESPONSE)