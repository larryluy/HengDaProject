from django.urls import path
from . import views

app_name = 'serviceApp'

urlpatterns = [
    path('download/', views.download, name='download'),
    path('platform/', views.platform, name='platform'),
]