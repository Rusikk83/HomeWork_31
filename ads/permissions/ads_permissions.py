from rest_framework.permissions import BasePermission

class IsModerator(BasePermission):

    message = 'Not permissions'

    def has_permission(self, request, view):
        if request.user.role == "moderator":
            return True
        else:
            return False
