from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

class paymentTypeViewSet(viewsets.ModelViewSet):

    queryset = models.paymentType.objects.all()
    serializer_class = serializers.paymentTypeSerializer

class paymentViewSet(viewsets.ModelViewSet):

    queryset = models.payment.objects.all()
    serializer_class = serializers.paymentSerializer


class orderViewSet(viewsets.ModelViewSet):

    queryset = models.order.objects.all()
    serializer_class = serializers.orderSerializer