from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class subscription(models.Model):
    subscription_id = models.AutoField(primary_key= True,null=False)
    customer_name = models.CharField(max_length=100,default='None',null=False)
    mobile_no = models.IntegerField(default=0000000000,null=False)
    email = models.CharField(max_length=1000,default='None',null=True)
    address = models.CharField(max_length=1000,default='None',null=False)
    subscriptionDuration = models.IntegerField(default=0,null=False)
    source_of_information = models.CharField(max_length=1000,default='None',null=True,blank=True)
    medical_condition = models.CharField(max_length=1000,default='None',null=True)
    payment_method = models.CharField(max_length=1000,default='None',null=False)
    juices = models.CharField(max_length=1000,default='None',null=False)
    quantity = models.IntegerField(default=1,null=False)
    created_on = models.DateTimeField(default="9999-12-31 23:59:59",null=False)
    updated_on = models.DateTimeField(default="9999-12-31 23:59:59",null=False)