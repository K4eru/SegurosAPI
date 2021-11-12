from . import models
from rest_framework import serializers

class paymentTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.paymentType
        fields = '__all__'

class paymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.payment
        fields = '__all__'
       
       # fields = (
       #     '__all__',
       # )

class orderSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.order
        fields = '__all__'

        #fields = (
        #    '__all__',
        #)
