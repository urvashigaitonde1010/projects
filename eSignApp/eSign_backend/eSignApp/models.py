
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    user_id = models.AutoField(primary_key= True,null=False)
    first_name = models.CharField(max_length=100,default='None',null=False)
    last_name = models.CharField(max_length=100,default='None',null=False)
    middle_name = models.CharField(max_length=100,default='None')
    # preffered_name = models.CharField(max_length=100,default='None',null=True)
    mobile_no = models.IntegerField(default=0000000000,null=False)
    email = models.CharField(max_length=1000,default='None',null=False)
    password = models.CharField(max_length=1000,default='None',null=False)
    organization = models.CharField(max_length=100,default='None',null=True)
    # gender = models.CharField(max_length=1000,default='None',null=False)
    street = models.CharField(max_length=1000,default='None',null=True)
    state = models.CharField(max_length=1000,default='None',null=True)
    city = models.CharField(max_length=1000,default='None',null=True)
    country = models.CharField(max_length=1000,default='None',null=True)
    zipcode = models.IntegerField(default=000000,null=True)
    default_image = models.IntegerField(default=0)
    created_on = models.DateTimeField(default="9999-12-31 23:59:59",null=False)
    updated_on = models.DateTimeField(default="9999-12-31 23:59:59",null=False)

class image(models.Model):
    image_id = models.AutoField(primary_key= True,null=False)
    user_id = models.IntegerField(default=0000000000,null=False)
    image = models.CharField(max_length=10000000000,default='None',null=False)
    preffered_name = models.CharField(max_length=10000,default='None',null=False)
    created_on = models.DateTimeField(default="9999-12-31 23:59:59",null=False)
    updated_on = models.DateTimeField(default="9999-12-31 23:59:59",null=False)