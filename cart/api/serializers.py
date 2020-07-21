from rest_framework import serializers

from ..models import Order

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status'),
