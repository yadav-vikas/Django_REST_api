#custom permissions
from rest_framework import permissions

class BasePermission(object):

    """
A base class from which all permission classes should inherit.
"""
    def has_permission(self,request,view):
        """
Return `True` if permission is granted, `False` otherwise.
"""
        return True
    
    def has_object_permission(self,request,view,obj):
        """
Return `True` if permission is granted, `False` otherwise.

To create our own custom permission, we will override the has_object_permission
method. Specifically we want to allow read-only for all requests but for any write
requests, such as edit or delete, the author must be the same as the current logged-in user
"""
        return True


