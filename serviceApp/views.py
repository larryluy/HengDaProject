from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def download(request):
    html = '<html><body>download</body></html>'
    return HttpResponse(html)

def platform(request):
    html = '<html><body>platform</body></html>'
    return HttpResponse(html)