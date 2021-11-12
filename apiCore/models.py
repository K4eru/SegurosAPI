from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey


class paymentType(models.Model):
    paymentName = models.CharField(max_length=20)        


class payment(models.Model):
    order = models.ForeignKey('order', on_delete= models.CASCADE)
    paymentType = models.ForeignKey('paymentType', on_delete= models.CASCADE)
    def __str__(self):
        return self.id


class order(models.Model):

    userID = models.CharField(max_length=20)
    orderType = models.CharField(max_length=20)
    nextPayment = models.DateField(blank=True, null=True)
    amount = models.IntegerField(default = 0)
    employeeID = models.CharField(max_length=20)
    dateVisit = models.DateField(blank=True, null=True)
    orderDescription = models.TextField()

    def __str__(self):
        return str(self.id)



class messageModel(models.Model):
    messages = models.CharField(max_length=200)

    def __str__(self):
        return self.messages