from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    message ='You must be owner'
    my_safe_method = ['GET']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        else:
            return request.user.is_admin



