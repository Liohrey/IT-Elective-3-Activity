from django.shortcuts import render

def index(request):
    return render(request, "pages/portfolio.html")

def about(request):
    return render(request, "pages/about.html")
