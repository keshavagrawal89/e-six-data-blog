from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a post to edit it.
    """
    def has_permission(self, request, view):
        if request.method in ['POST', 'PATCH', 'PUT', 'DELETE']:
            return request.user.is_authenticated

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the post.
        return obj.author == request.user
