from django.http import HttpResponse

from articles.models import Article

#from database
article_obj = Article.objects.get(id=1)

article_title = article_obj.title
article_content = article_obj.content


name = "Solomon"
HTML_RESPONSE = f"""
<h1> {article_obj.id} article_title</h1>
<h4>article_content</h4>
"""

def home(request):
    return HttpResponse(HTML_RESPONSE)