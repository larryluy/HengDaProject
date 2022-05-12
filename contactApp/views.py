from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def contact(request):
    html = '<html><body>contact</body></html>'
    return HttpResponse(html)

def recruit(request):
    html = '<html><body>recruit</body></html>'
    return HttpResponse(html)