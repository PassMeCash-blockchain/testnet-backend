from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from django.conf import settings
from django.contrib.auth.models import User
import requests as req, uuid

from .models import UserDetail as UD, Stage
from .serializers import (
    UserCreateSerializer as ucs
)

from .utils import *

T = True
F = False

class RegisterView(APIView):

    def post(self, request):
        r = request
        data = r.data
        if data['path'] == 'create':
            if UD.objects.filter(phone_number=data['phone_number']).exists():
                return Response({'phone_number': 'Phone number has been used.'}, status=status.HTTP_400_BAD_REQUEST)

            
            serializer = ucs(data={"username": str(uuid.uuid4()),
                            "password": data['password']})

            # serializer = ucs(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.create(serializer.validated_data)
            UD.objects.create(user=userInfo(user.username),
                            phone_number=data['phone_number'])
            otp = T
            if otp:
                Stage.objects.create(user=user,stageOne=T)
                UD.objects.filter(user=userInfo(
                    user.username)).update(verified=T)
                res = req.post(f"{BaseUrl(r)}/auth/token/", data={"username":user.username, "password": data['password']})
                res = {**res.json(), "uuid":user.username, "stage":'step one', "otp":'sent'}
            else:
                res = {"uuid": user.username, "stage": "step two", 'otp': "not sent"}

            return Response(res, status=status.HTTP_200_OK)
        
        if data['path'] == "personal-info":

            if not User.objects.filter(username=data['uuid']).exists():
                return Response({'user': f"No user with uuid {data['uuid']}."}, status=status.HTTP_404_NOT_FOUND)
            
            res = ucs.personal(data)

            if res["message"] == 'done':
                return Response({"uuid": data['uuid'], "stage": 'step three'}, status=status.HTTP_200_OK)
            else:
                return Response({"error": res["message"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if data['path'] == "contact-info":

            if not User.objects.filter(username=data['uuid']).exists():
                return Response({'user': f"No user with uuid {data['uuid']}."}, status=status.HTTP_404_NOT_FOUND)

            res = ucs.contact(data)

            if res["message"] == 'done':
                return Response({"uuid": data['uuid'], "stage": 'completed'}, status=status.HTTP_200_OK)
            else:
                return Response({"error": res["message"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckInfoView(APIView):

    def get(self, request):
        try:
            token = request.headers['X-Self']
            if Key == token:
                req = request.query_params
                if req['type'] == 'email':
                    email = req['email']
                    useEmail = User.objects.get(email=email)
                    print(useEmail)
                    if useEmail.exists():
                        return Response({"username": useEmail.username}, status=status.HTTP_200_OK)
                    else:
                        return Response({}, status=status.HTTP_404_NOT_FOUND)
                else:
                    phone = req['phone']
                    useNumber = UD.objects.filter(phone_number=phone)
                    if useNumber.exists():
                        return Response({"username": useNumber.user.username}, status=status.HTTP_200_OK)
                    else:
                        return Response({}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(e)
            return Response({"error": "FORBIDDEN"}, status=status.HTTP_403_FORBIDDEN)



        
