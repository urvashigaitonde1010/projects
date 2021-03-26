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
from .models import *
from django.core.mail import send_mail
import string
import random
import base64
import codecs
from PIL import Image
# Create your views here.
@api_view(['GET', 'POST'])
# @csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        print(request.body)
        signUpJson = json.loads(request.body.decode("utf-8"))
        # print(signUpJson)
        signUpSerializer = SignUpSerializer(data=signUpJson)
        # print(signUpnSerializer)
        if signUpSerializer.is_valid():
            # print(SignUpSerializer.data())
            email = signUpSerializer.validated_data['email']
            entries = len(user.objects.filter(email = email).values())
            if(entries>0):
                return Response("User already exist.")
            now = datetime.datetime.now()
            signUpSerializer.save(created_on = now,updated_on = now )
            return Response("Saved")
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        signInJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        signInSerializer = SignInSerializer(data=signInJson)
        #rint(signUpnSerializer)
        if signInSerializer.is_valid():
            # print(SignUpSerializer.data())
            email = signInSerializer.data['email']
            password = signInSerializer.data['password']
            try:
                pass_from_db = user.objects.filter(email = email).values("password")[0]['password']
                print(pass_from_db)
                if(password == pass_from_db):
                    user_id = user.objects.filter(email = email).values("user_id")[0]['user_id']
                    return Response("Authentication passed-"+str(user_id))
                else:
                    return Response("Authentication failed.")
            except:
                return Response("Authentication failed.")
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        uploadJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        uploadSerializer = UploadSerializer(data=uploadJson)
        #rint(signUpnSerializer)
        if uploadSerializer.is_valid():
            # print(SignUpSerializer.data())
            now = datetime.datetime.now()
            uploadSerializer.save(created_on = now,updated_on = now )
            user_id1 = uploadSerializer.data['user_id']
            try:
                data1 = uploadSerializer.data['image']
                data = data1.split(",")[1]
                # print(data)
                # message_bytes = img_data1.encode('ascii')
                # encodedBytes = base64.b64encode(data.encode("utf-8"))            
                with open("imageToSave.png", "wb") as fh:
                    fh.write(base64.b64decode(data))
                img = Image.open('imageToSave.png')
                img = img.convert("RGBA")
                datas = img.getdata()

                newData = []
                for item in datas:
                    if item[0] >= 230 and item[1] >= 230 and item[2] >= 230:
                        newData.append((255, 255, 255, 0))
                    else:
                        newData.append(item)

                img.putdata(newData)
                # print(newData)
                img.save("img.png", "PNG")
                with open("img.png", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    # encoded_string = 
                    encoded_string1 = "data:image/png;base64,"+ encoded_string.decode('utf-8')
                    # print()
                    image_id = image.objects.filter(user_id = user_id1).values('image_id').order_by('-created_on')[0]['image_id']
                    imageData = image.objects.get(image_id = image_id)
                    imageData.image = encoded_string1
                    imageData.save()
                    print(image_id)
            except:
                print("exception occured")
            
            image_entries = image.objects.filter(user_id = user_id1).values()
            # print(image_entries)
            if(len(image_entries) == 1):
                user1 = user.objects.get(user_id = user_id1)
                imageid = image.objects.filter(user_id = user_id1).values("image_id")[0]['image_id']
                # fh.write(encodedBytes)
                user1.default_image = imageid
                user1.save()
            return Response("Image uploaded.")
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def get_details(request):
    if request.method == 'POST':
        getdetailsJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        getdetailsSerializer = GetdetailsSerializer(data=getdetailsJson)
        #rint(signUpnSerializer)
        if getdetailsSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(getdetailsSerializer)
            email = getdetailsSerializer.data['email']
            # print(userid)
            details = user.objects.filter(email = email).values()
            return Response(details[0])
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def get_images(request):
    if request.method == 'POST':
        getdetailsJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        getdetailsSerializer = GetdetailsSerializer(data=getdetailsJson)
        #rint(signUpnSerializer)
        if getdetailsSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(getdetailsSerializer)
            email = getdetailsSerializer.data['email']
            # print(userid)
            userid = user.objects.filter(email = email).values('user_id')[0]['user_id']
            # return Response(details[0])
            details = image.objects.filter(user_id = userid).values()
            return Response(details)
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        getdetailsJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        getdetailsSerializer = GetdetailsSerializer(data=getdetailsJson)
        #rint(signUpnSerializer)
        if getdetailsSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(getdetailsSerializer)
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            pwdSize = 8
            passwordString = ''.join((random.choice(chars)) for x in range(pwdSize))
            email = getdetailsSerializer.data['email']
            # print(use
            success = 0
            # print(len(user.objects.filter(email=email).values()))
            if len(user.objects.filter(email=email).values())>0:
                success = send_mail('Code to reset your password for eSign app','Hi,\n\nPlease entere the following code in the ESign App to authenticate your email and change your password.\n\nCode: '+passwordString+'\n\nPlease do not reply to this email. This is auto generated email.\n\nThank you.','noreply.esignapp@gmail.com',[email],fail_silently=False,)
            # return Response(details[0])
            # details = image.objects.filter(user_id = userid).values()
            if success == 1:
                return Response(passwordString)
            return Response("failure")
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        changePasswordJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        changePasswordSerializer = SignInSerializer(data=changePasswordJson)
        #rint(signUpnSerializer)
        if changePasswordSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(changePasswordSerializer)
            email = changePasswordSerializer.data['email']
            password = changePasswordSerializer.data['password']
            # print(userid)
            u = user.objects.get(email = email)
            u.password = password
            u.save()
            # return Response(details[0])
            # details = image.objects.filter(user_id = userid).values()
            return Response("password changed.")
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def get_default_image(request):
    if request.method == 'POST':
        getdetailsJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        getdetailsSerializer = GetdetailsSerializer(data=getdetailsJson)
        #rint(signUpnSerializer)
        if getdetailsSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(getdetailsSerializer)
            email = getdetailsSerializer.data['email']
            # print(userid)
            details = user.objects.filter(email = email).values("default_image")[0]['default_image']
            return Response(details)
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def get_default_preffered_name(request):
    if request.method == 'POST':
        getdetailsJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        getdetailsSerializer = GetdetailsSerializer(data=getdetailsJson)
        #rint(signUpnSerializer)
        if getdetailsSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(getdetailsSerializer)
            email = getdetailsSerializer.data['email']
            # print(userid)
            details = user.objects.filter(email = email).values("default_image")[0]['default_image']
            pref_name = ""
            if details != 0:
                pref_name = image.objects.filter(image_id = details).values("preffered_name")[0]['preffered_name']
            return Response(pref_name)
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def set_default_image(request):
    if request.method == 'POST':
        getdetailsJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        getdetailsSerializer = SetDefaultImageSerializer(data=getdetailsJson)
        #rint(signUpnSerializer)
        if getdetailsSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(getdetailsSerializer)
            email = getdetailsSerializer.data['email']
            # print(userid)
            details = user.objects.get(email = email)
            details.default_image = getdetailsSerializer.data['default_image']
            details.save()
            return Response("updated default image")
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def edit_details(request):
    if request.method == 'POST':
        getdetailsJson = json.loads(request.body.decode("utf-8"))
        #print(signUpJson)
        getdetailsSerializer = EditDetailsSerializer(data=getdetailsJson)
        #rint(signUpnSerializer)
        if getdetailsSerializer.is_valid():
            # print(SignUpSerializer.data())
            print(getdetailsSerializer)
            email = getdetailsSerializer.data['email']
            # print(userid)
            details = user.objects.get(email = email)
            details.state = getdetailsSerializer.data['state']
            details.country = getdetailsSerializer.data['country']
            details.street = getdetailsSerializer.data['street']
            details.city = getdetailsSerializer.data['city']
            details.zipcode = getdetailsSerializer.data['zipcode']
            details.organization = getdetailsSerializer.data['organization']
            details.mobile_no = getdetailsSerializer.data['mobile_no']
            details.save()
            return Response("Updated")
        else:
            return Response("Invalid Serializer")

@api_view(['GET', 'POST'])
@csrf_exempt
def erase(request):
    if request.method == 'GET':
        user.objects.all().delete()
        return Response("erased")