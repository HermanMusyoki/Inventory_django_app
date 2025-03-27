from django.http import HttpResponse

name = "Solomon"
HTML_RESPONSE = f"""
<h1>Hello {name}</h1>
"""

def home(request):
    return HttpResponse(HTML_RESPONSE)