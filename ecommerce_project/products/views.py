from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product
from .serializers import ProductSerializer

# Product ViewSet for CRUD operations
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Permissions
    permission_classes = [IsAuthenticated]  # All users must be authenticated to interact with the products

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]  # Only admins can create, update or delete products
        return super().get_permissions()

    def get_queryset(self):
        """
        Filter products by category or name if provided in the query params.
        """
        queryset = Product.objects.all()

        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if category:
            queryset = queryset.filter(category__icontains=category)

        return queryset

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# products/views.py
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'price', 'created_date']
    search_fields = ['name', 'category__name']

# products/views.py
from django.http import JsonResponse

def some_view_function(request):
    return JsonResponse({'message': 'This is the response from /api/endpoint/'})
