from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = "you must be th owner of this object."

    # def has_permission(self, request, view):
    #     return request.method in SAFE_METHODS

    def has_object_permission(self, request, view ,obj):
        return obj.user == request.user