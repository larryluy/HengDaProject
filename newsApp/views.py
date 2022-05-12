from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def company(request):
    html = '<html><body>company</body></html>'
    return HttpResponse(html)

def industry(request):
    html = '<html><body>industry</body></html>'
    return HttpResponse(html)

def notice(request):
    html = '<html><body>notice</body></html>'
    return HttpResponse(html)