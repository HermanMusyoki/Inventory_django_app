from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

#from database
article_obj = Article.objects.get(id=1)


context = {
    "id" : article_obj.id,
    "title" : article_obj.title,
    "content" : article_obj.content,

}
#article_title = article_obj.title
#article_content = article_obj.content


HTML_RESPONSE = render_to_string("home.html",context= context)
#HTML_RESPONSE = """
#<h1> {id} {title}</h1>
#<h4>{content}</h4>
#""".format(**context)

def home(request):
    return HttpResponse(HTML_RESPONSE)