from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

ORDER_TYPES = ((0, 'Normal' ),
                (1, 'Especial'))


class company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # responsable = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_all_companies():
        return company.objects.all()
    
    def get_company(id):
        return company.objects.get(id=id)

class training(models.Model):
    name=models.CharField(max_length=100)
    professionalAssigned = models.IntegerField()
    client1 = models.IntegerField(blank= False)
    client2 = models.IntegerField(blank= False)
    client3 = models.IntegerField(blank= False)
    date = models.DateField()

    def __str__(self):
        return self.name


class order(models.Model):
    userID = models.IntegerField()
    type =  models.IntegerField(choices=ORDER_TYPES, default=0)
    nextPayment = models.DateField(default='1970-01-01')
    amount = models.IntegerField(default=0)
    employeeID = models.IntegerField()
    dateVisit = models.DateField(default='1970-01-01')
    description = models.TextField(blank=True)
    improvement = models.TextField(blank=True)
    edited = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    def get_all_orders():
        return order.objects.all()

    def get_order(id):
        return order.objects.get(id = id)

    def orderByEmployee(id):
        return order.objects.get(employeeID = id)

class checklist(models.Model):
    orderID = models.IntegerField()
    title= models.CharField(max_length=100)
    professionalAssigned = models.IntegerField()
    question1 = models.CharField(max_length=100,blank=True)
    answer1 = models.CharField(max_length=100,blank=True)
    question2 = models.CharField(max_length=100,blank=True)
    answer2 = models.CharField(max_length=100,blank=True)
    question3 = models.CharField(max_length=100,blank=True)
    answer3 = models.CharField(max_length=100,blank=True)
    question4 = models.CharField(max_length=100,blank=True)
    answer4 = models.CharField(max_length=100,blank=True)
    question5 = models.CharField(max_length=100,blank=True)
    answer5 = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title

    def get_checklist(id):
        return checklist.objects.get(id = id)

