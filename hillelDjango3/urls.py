"""
URL configuration for hillelDjango3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import celery_view, top_selling_products_view
from products.viewsets import ProductViewSet, OrderViewSet, RecipeViewSet, StoreViewSet, StoreInventoryViewSet
from telegram.views import telegram
from products.tasks import today_count_orders as today_count_orders_view

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('recipes', RecipeViewSet)
router.register('stores', StoreViewSet)
router.register('store-inventories', StoreInventoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('telegram/', telegram),
    path('celery/', celery_view),
    path("today_count_orders/", today_count_orders_view),
    path("top_selling_products/", top_selling_products_view),
    path("__debug__/", include("debug_toolbar.urls")),
]
