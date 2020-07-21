from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsSeller(BasePermission):
    message = "You must be the seller for this product in order to update its properties."
    # my_safe_methods = ['GET','PUT']
    # def has_permission(self,request,view):
    #     if request.method in my_safe_methods:
    #         return True
    #     return False
    def has_object_permission(self,request,view,obj):
        if request.method == SAFE_METHODS:
            return True
        return obj.seller == request.user.profile
