from django.http import HttpResponse

HTML_RESPONSE = """
<h1>Hello Solomon</h1>
"""

def home(request):
    return HttpResponse(HTML_RESPONSE)