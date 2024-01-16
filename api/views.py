import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Order
from .serializers import *

# Create your views here.

@api_view(['POST'])
def add_order(request):
    params = json.loads(request.body)
    phone_number = params["phoneNumber"]
    chosen_operator = params["chosenOperator"]
    minutes_selected_option = params["minutesSelectedOption"]
    internet_selected_option = params["internetSelectedOption"]
    rent = params["rent"]
    redeem = params["redeem"]
    socials = params["socials"]
    total_amount = params["totalAmount"]
    order = Order.objects.create(phoneNumber=phone_number, operator=chosen_operator,
                                 minutesOption=minutes_selected_option, internetOption=internet_selected_option,
                                 rent=rent, redeem=redeem, socials=socials, totalAmount=total_amount)
    order.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def orders_list(request):
    data = Order.objects.all()
    serialzier = OrderSerializer(data, context={'request': request}, many=True)
    return Response(serialzier.data)

@api_view(['DELETE'])
def clear(request):
    Order.objects.all().delete()
    return Response(status=status.HTTP_200_OK)