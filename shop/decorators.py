from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from .models import Shop

def is_shop_owner(function):
    def wrap(request,shop_id,*args,**kwargs):
        if request.user.profile != Shop.objects.get(id=shop_id).owner:
            raise PermissionDenied
        else:
            return function(request,shop_id,*args,**kwargs)
    return wrap
