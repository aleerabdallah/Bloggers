from rest_framework.permissions import BasePermission








class IsOwnerOrReadOnly(BasePermission):
    message = "You don't have permission to delete or edit"
    def has_object_permission(self, request, view, obj):

        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        
        # return super().has_object_permission(request, view, obj)
        return obj.author == request.user