from django.shortcuts import render
from django.utils.timezone import make_aware
import pytz
import pyotp
import base64
import uuid
from datetime import datetime
from rest_framework.views import APIView
import arrow
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *
# Create your views here.

def GenTime():
    time_uni=arrow.utcnow()
    local_time=time_uni.to('Africa/Lagos')
    return local_time
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + 'hsgsvehdhdb'

class RequestOTP(APIView):
    time=GenTime()

    def get(self,request):
        return Response('Generate your Otp')

    def post(self,request):
        data=request.data
        phone=data['phone']
        try:
            Mobile = phoneModel.objects.get(Mobile=data['phone'])  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = phoneModel.objects.get(Mobile=data['phone'])  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        if Mobile.counter>=6 and Mobile.wait_time is None:
            naive_date_str=str(self.time.shift(hours=1).format('YYYY-MM-DD HH:mm'))
            naive_datetime=datetime.strptime(naive_date_str, '%Y-%m-%d %H:%M')
            Mobile.wait_time = make_aware(naive_datetime, timezone=pytz.timezone("Africa/Lagos"))
            Mobile.save()
            return Response({'disallowed':'maximum otp call exceeded'})
        elif Mobile.counter>=6 and Mobile.wait_time:
                return Response({'message':"cannot create otp now, please exceed wait time"})
        Mobile.save()
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(data['phone']).encode())  # Key is generated
        OTP = pyotp.HOTP(key)
        # Call SMS Service
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  #

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
         # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"] , Mobile.counter):  # Verifying the OTP
            return Response({'success':"Verification Successful"}, status=200)
        return Response("OTP is wrong", status=400)

class ResetOTP(APIView):
    time=datetime.strptime(GenTime().format('YYYY-MM-DD HH:mm'), '%Y-%m-%d %H:%M')
    time=make_aware(time, timezone=pytz.timezone("Africa/Lagos"))
    def get(self,request):
        data=phoneModel.objects.all()
        due_numbers=[]
        for i in data:
            if i.wait_time is not None:
                if i.wait_time>self.time:
                    due_numbers.append(i)
                    due_phone=phoneModel.objects.get(id=i.id)
                    due_phone.counter=0
                    due_phone.wait_time=None
                    due_phone.save()
        if len(due_numbers)>0:
            return Response({"message":f"found {len(due_numbers)} numbers and resolved them"})
        else:
            return Response({"message":"No due numbers found"})


