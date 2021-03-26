from rest_framework import serializers
from django import forms
from .models import *
from django.contrib.auth.models import User

class SignUpSerializer(serializers.ModelSerializer):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('first_name','last_name','middle_name','mobile_no','email','password','organization') 

class SignInSerializer(serializers.ModelSerializer):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('email','password') 

class UploadSerializer(serializers.ModelSerializer):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = image
        fields = ('user_id','image','preffered_name') 

class GetdetailsSerializer(serializers.ModelSerializer):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('user_id','email') 

class SetDefaultImageSerializer(serializers.ModelSerializer):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('user_id','email','default_image') 

class EditDetailsSerializer(serializers.ModelSerializer):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = ('email','organization','mobile_no','state','street','city','country','zipcode') 