from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
import json
from .serializers import *
import datetime
# Create your views here.
@api_view(['GET', 'POST'])
@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        subscriptionJson = json.loads(request.body.decode("utf-8"))
        subscriptionSerializer = SubscriptionSerializer(data=subscriptionJson)
        if subscriptionSerializer.is_valid():
            now = datetime.datetime.now()
            subscriptionSerializer.save(created_on = now,updated_on = now )
            return Response("Saved")
        else:
            return Response("Invalid Serializer")


