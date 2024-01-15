from rest_framework import serializers
from api.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'phoneNumber', 'operator', 'minutesOption', 'internetOption',
                  'rent', 'redeem', 'socials', 'totalAmount']