from rest_framework.permissions import BasePermission

class IsCurrentUserOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return obj.colecionador == request.user
