from django.shortcuts import render
import pyotp
import base64
import uuid
from datetime import datetime
from rest_framework import permissions, status
from rest_framework.views import APIView
import arrow
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import *
# Create your views here.

def GenTime():
    time_uni=arrow.utcnow()
    local_time=time_uni.to('Africa/Lagos')
    return local_time
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + 'hsgsvehdhdb'


class createUpdateOtp(APIView):

    def get(self,request):
        return Response('Generate your Otp')

    def post(self,request):
        data=request.data
        phone=data['phone']
        Mobile = phoneModel.objects.get_or_create(Mobile=phone)  # if Mobile already exists the take this else create New One
        Mobile = Mobile[0]
        if Mobile.counter == 6:
            Mobile.counter += 1
            Mobile.save()
            return Response({'message': {"disallowed": 'maximum otp call exceeded', "wait_time": str(Mobile.wait_time)}}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            if Mobile.wait_time is not None:
                return Response({'message': {"disallowed": "Cannot create otp now, Please exceed wait time", "wait_time": str(Mobile.wait_time)}}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                # Used in production
                # keygen = generateKey()
                # key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
                # print(key)
                # OTP = pyotp.HOTP(key)
                # send otp function
                Mobile.counter += 1  
                OTP = '654321'
                # phoneModel.objects.filter(Mobile=phone).update(
                #     counter=Mobile.counter + 1)  # Update Counter At every Call
                Mobile.save()
                if Mobile.counter == 6:
                    Mobile.wait_time = GenTime().shift(
                        hours=1).format('YYYY-MM-DD HH:mm')
                    Mobile.save()
                print(Mobile)
                return Response({"success": Mobile.counter}, status=status.HTTP_200_OK)
                # return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  #

class VerifyOtp(APIView):

    def get(self,request):
        return Response('Verify Your OTP')
    def post(self,request):
        data=request.data
        phone=data['phone']
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        print(key) # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"] , Mobile.counter):  # Verifying the OTP
            return Response({'success':"Verification Successful"}, status=200)
        return Response("OTP is wrong", status=400)

class ResetOtp(APIView):
    def get(self,request):
        pass


# b'GA4TAMRUGAZDAMRTFUYDILJRGVUHGZ3TOZSWQZDIMRRA===='
# b'GA4TAMRUGAZDAMRTFUYDILJRGVUHGZ3TOZSWQZDIMRRA===='
