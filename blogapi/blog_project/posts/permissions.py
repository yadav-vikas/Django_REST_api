#custom permissions
from rest_framework import permissions

# class BasePermission(object):

#     """
# A base class from which all permission classes should inherit.
# """
#     def has_permission(self,request,view):
#         """
# Return `True` if permission is granted, `False` otherwise.
# """
#         return True
    
#     def has_object_permission(self,request,view,obj):
#         """
# Return `True` if permission is granted, `False` otherwise.

# To create our own custom permission, we will override the has_object_permission
# method. Specifically we want to allow read-only for all requests but for any write
# requests, such as edit or delete, the author must be the same as the current logged-in user
# """
#         return True


class IsAuthorOrReadOnly(permissions.BasePermission):
    """We import permissions at the top and then create a custom class IsAuthorOrReadOnly
which extends BasePermission. Then we override has_object_permission. If a request
contains HTTP verbs included in SAFE_METHODS–a tuple containing GET, OPTIONS, and
HEAD–then it is a read-only request and permission is granted.

Otherwise the request is for a write of some kind, which means updating the API
resource so either create, delete, or edit functionality. In that case, we check if the
author of the object in question, which is our blog post obj.author matches the user
making the request request.user

    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
