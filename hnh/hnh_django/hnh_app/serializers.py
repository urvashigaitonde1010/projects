from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = ('customer_name','email','mobile_no','address','subscriptionDuration','source_of_information','medical_condition','payment_method','juices','quantity') 