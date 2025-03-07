"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import ItemsListView, ItemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints for items
    path('api/items/', ItemsListView.as_view(), name='items-list'),
    path('api/items/add/', ItemsListView.as_view(), name='items-add'),
    path('api/items/<int:item_id>/', ItemDetailView.as_view(), name='item-detail'),
    path('api/items/update/<int:item_id>/', ItemDetailView.as_view(), name='item-update'),
    path('api/items/delete/<int:item_id>/', ItemDetailView.as_view(), name='item-delete'),
]
