from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
import string, random, uuid, json, requests as req
# Create your views here.

from .utils import *
from .schemas import *

T = True
F = False

from .serializers import (
    UserCreateSerializer as ucs
)

url = URLs["authUrl"]
otpUrl = URLs["otpUrl"]

class RegisterView(APIView):
    """Creates new users.
        > step 1 requires [Phone number, password & path = 'create']
        > step 2 requires [uuid or access token in header, first name,last name, email, DOB & path = 'personal-info']
        > step 3 requires [uuid or access token in header, state, lga, address, addreaa alt(optional) & path = 'contact-info']
    """

    summary = "Create User"

    tags = ["Account"]
    post_tag = ['Registration']
    request_schema = RegisterRequestSchema

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
        data = request.data
        login = data['login']

        _type = 'phone'
        if login.startswith('+'):
            initLogin = login
            login = login[1:]
        if '@' in login:
            _type = 'email'
        params = {"type": _type}
        params[_type] = login
        _res = req.get(f"{url}auth/v1/check", params = params, headers={"X-Self": Key})
        if _res.status_code == 401:
            return Response({"error": "UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)
        if _res.status_code == 403:
            return Response({"error": "FORBIDDEN"}, status=status.HTTP_403_FORBIDDEN)
        if _res.status_code == 404:
            return Response({"message": "No account found with the given cridentials."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        if _res.status_code == 200:
            loginData = {"username": _res.json()['username'], "password": data['password']}
            res = req.post(f"{url}auth/token/", data = loginData,)
            ress = res.json()
            req.post(f"{url}auth/v1/lastlogin", headers={"Authorization": f"Bearer {ress['access']}"})
            if res.status_code == 200:
                # get more details
                __res = req.get(f"{url}auth/v1/getmorelogininfo", headers={"Authorization": f"Bearer {ress['access']}", "X-Self": Key})
                ___res = {**ress, **__res.json()}
                return Response({"message": ___res}, status=status.HTTP_200_OK)
            else:
                err = list(res.json().keys())
                Errors = []
                for i in range(len(err)):
                    Errors.append(ress[err[i]])
                return Response({"message": Errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
