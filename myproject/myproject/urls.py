from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls', namespace="portfolio")),
    path('dashboard/', include('dashboard.urls', namespace="dashboard")),
    path('', include('portfolio.urls', namespace="portfolio")),
]
