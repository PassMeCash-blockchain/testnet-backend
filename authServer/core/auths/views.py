from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from django.conf import settings
from django.contrib.auth.models import User
import requests as req, uuid

from .models import (
    UserDetail as UD,
    Stage,
    LastLogin as LL,
)
from .serializers import (
    UserCreateSerializer as ucs,
    UserSerializer as us,
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
            otp = req.post(f"{BaseUrl(r)}/otp/v1/create-or-update",
                           data={"phone": data["phone_number"], "password": data['password']})
            if otp.status_code == 200:
                Stage.objects.create(user=user,stageOne=T)
                UD.objects.filter(user=userInfo(
                    user.username)).update(verified=T)
                res = req.post(f"{BaseUrl(r)}/auth/token/", data={"username":user.username, "password": data['password']})
                res = {**res.json(), "uuid":user.username, "registration_stage":'step one', "otp":otp.json()}
            else:
                res = {"uuid": user.username, "registration_stage": "step two", 'otp': otp.json()}

            return Response(res, status=status.HTTP_200_OK)
        
        elif data['path'] == "personal-info":

            if not User.objects.filter(username=data['uuid']).exists():
                return Response({'user': f"No user with uuid {data['uuid']}."}, status=status.HTTP_404_NOT_FOUND)
            
            res = ucs.personal(data)

            if res["status"] == 200:
                return Response({"uuid": data['uuid'], "registration_stage": 'step three'}, status=status.HTTP_200_OK)
            else:
                return Response({"error": res["message"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        elif data['path'] == "contact-info":

            if not User.objects.filter(username=data['uuid']).exists():
                return Response({'user': f"No user with uuid {data['uuid']}."}, status=status.HTTP_404_NOT_FOUND)

            res = ucs.contact(data)

            if res["status"] == 200:
                return Response({"uuid": data['uuid'], "registration_stage": 'completed'}, status=status.HTTP_200_OK)
            else:
                return Response({"error": res["message"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "No path"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CheckInfoView(APIView):

    def get(self, request):
        try:
            token = request.headers['X-Self']
            if Key == token:
                query = request.query_params
                if query['type'] == 'email':
                    email = query['email']
                    useEmail = User.objects.filter(email=email)
                    if useEmail.exists():
                        for i in useEmail:
                            username = i.username
                        return Response({"username": username}, status=status.HTTP_200_OK)
                    else:
                        return Response({}, status=status.HTTP_404_NOT_FOUND)
                else:
                    phone = query['phone']
                    useNumber = UD.objects.filter(phone_number=phone)
                    if useNumber.exists():
                        return Response({"username": useNumber.user.username}, status=status.HTTP_200_OK)
                    else:
                        return Response({}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": "FORBIDDEN"}, status=status.HTTP_403_FORBIDDEN)


class GetMoreInfoView(APIView):

    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            token = request.headers['X-Self']
        except Exception as e:
            print(e)
            return Response({"error": "FORBIDDEN"}, status=status.HTTP_403_FORBIDDEN)
        if Key == token:
            user = request.user
            res = us.login(user)
            if res["status"] == 200:
                return Response(res['message'], status=status.HTTP_200_OK)
            else:
                return Response({"error": res["message"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)
        


class createLastLogin(APIView):

    permissions_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user

        res = us.lastlogin(user)
        if res["status"] == 200:
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({"error": res["message"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



        
