from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
import string, random, uuid, json, requests as req
# Create your views here.

from .utils import *

T = True
F = False

from .serializers import (
    UserCreateSerializer as ucs
)

url = URLs["authUrl"]
class RegisterView(APIView):

    def post(self, request):
        res = req.post(f"{url}auth/v1/register", data = request.data)
        ress = res.json()
        err = list(res.json().keys())
        Errors = []
        if res.status_code == 200:
            return Response({"message": res.json()}, status=status.HTTP_200_OK)
        
        if res.status_code == 400:

            for i in range(len(err)):
                if err[i] == 'password':
                    Errors.append(ress[err[i]])
                if err[i] == 'phone_number':
                    Errors.append(ress[err[i]])
                else:
                    Errors.append(ress[err[i]])
            return Response({"message": Errors}, status=status.HTTP_200_OK)
        
        if res.status_code == 404:
            for i in range(len(err)):
                Errors.append(ress[err[i]])
            return Response({"message": Errors}, status=status.HTTP_404_NOT_FOUND)
        
        if res.status_code == 500:
            for i in range(len(err)):
                Errors.append(ress[err[i]])
            return Response({"message": Errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    
    def post(self, request):
        params = {"type": "email"}
        params["email"] = "asss@aaa.com"
        _res = req.get(f"{url}auth/v1/check", params = params, headers={"X-Self": Key})
        print(_res.json(), _res.status_code)
        bearer = request.headers['Authorization']
        res = req.post(f"{url}auth/token/", data = request.data, headers={"Authorization": bearer})
        ress = res.json()
        if res.status_code == 200:
            return Response({"message": ress}, status=status.HTTP_200_OK)
        else:
            err = list(res.json().keys())
            Errors = []
            for i in range(len(err)):
                Errors.append(ress[err[i]])
            return Response({"message": Errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
