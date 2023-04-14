from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
import string, random, uuid, json, requests
# Create your views here.

from .utils import *

T = True
F = False

class RegisterView(APIView):

    def post(self, request):
        res = requests.post(f"{authUrl}auth/v1/register", data ={'key':'value'})
        print(res)
        return Response({"message": res.json()}, status=status.HTTP_200_OK)