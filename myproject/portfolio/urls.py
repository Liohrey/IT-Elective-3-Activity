from django.urls import path
from .views import index, about

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
