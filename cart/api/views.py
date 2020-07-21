from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView
from .serializers import OrderUpdateSerializer

from ..models import Order

class OrderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
