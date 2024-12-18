from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

from django.urls import path
from . import views  # Import the views from your app

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),  # URL for creating and listing products
]

# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from . import views

urlpatterns = [
    path('api/endpoint/', views.some_view_function, name='some-view'),  # Custom endpoint
]
