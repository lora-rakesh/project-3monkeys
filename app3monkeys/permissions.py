from rest_framework import permissions

class IsAdminOrLimitedAccess(permissions.BasePermission):
    """
    - Admins (is_staff or superuser) → full CRUD
    - Normal users → only GET and POST
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_staff or request.user.is_superuser:
            return True  # Admin → allow all methods

        # Normal user → only GET & POST
        return request.method in ['GET', 'POST']
