# permissions.py
from rest_framework.permissions import IsAuthenticated

class ProductPermission(IsAuthenticated):
    def has_permission(self, request, view):
        # Allow access to the product-related endpoints for authenticated users only
        if request.method in ['POST', 'PUT', 'DELETE']:
            return request.user.is_authenticated
        return True
