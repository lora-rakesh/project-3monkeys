# permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    - Admins (is_staff or superuser) → full CRUD
    - Normal users → only GET (no POST)
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_staff or request.user.is_superuser:
            return True  # Admin → allow all methods

        # Normal user → only safe methods (GET, HEAD, OPTIONS)
        return request.method in permissions.SAFE_METHODS


class IsAdminOrReadWrite(permissions.BasePermission):
    """
    - Admins (is_staff or superuser) → full CRUD
    - Normal users → GET and POST (no PUT, PATCH, DELETE)
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_staff or request.user.is_superuser:
            return True  # Admin → allow all methods

        # Normal user → only GET and POST
        return request.method in ['GET', 'POST', 'HEAD', 'OPTIONS']


class IsAdminOrLimitedAccess(permissions.BasePermission):
    """
    Your original permission class - keep it for backward compatibility
    - Admins (is_staff or superuser) → full CRUD
    - Normal users → GET and POST
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_staff or request.user.is_superuser:
            return True

        return request.method in ['GET', 'POST', 'HEAD', 'OPTIONS']