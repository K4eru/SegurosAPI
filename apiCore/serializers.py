from . import models
from rest_framework import serializers

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.order
        fields = '__all__'

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.company
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     demo = models.company.objects.get(pk=instance.id)
    #     models.company.objects.filter(pk=instance.id).update(**validated_data)
    #     return demo

class trainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.training
        fields = '__all__'

class checklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.checklist
        fields = '__all__'


   