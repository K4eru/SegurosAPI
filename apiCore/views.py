from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import response, viewsets
from . import serializers
from . import models
import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

class orderViewSet(viewsets.ModelViewSet):
    queryset = models.order.objects.all()
    serializer_class = serializers.orderSerializer

    def create(self,request):
        var = request.data
        var.save()
        return Response(data="paso")

    
class companyViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
    
    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = serializers.companySerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")
    queryset = models.company.objects.all()
    serializer_class = serializers.companySerializer

class trainingViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
    
    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = serializers.companySerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")
    queryset = models.training.objects.all()
    serializer_class = serializers.trainingSerializer

class checklistViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
    
    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = serializers.companySerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")
    queryset = models.checklist.objects.all()
    serializer_class = serializers.checklistSerializer

