from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
import string, random, uuid, json, requests
# Create your views here.

from .utils import *

T = True
F = False

from .serializers import (
    UserCreateSerializer as ucs
)

class RegisterView(APIView):

    def post(self, request):

        serializer = ucs(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.create(serializer.validated_data)
        user = us(user)

        gU = User.objects.get(username=username)

        gU.first_name = first_name
        gU.last_name = last_name
        gU.save()

        x = AI()
        x.first_name = first_name
        x.last_name = last_name
        x.username = username
        x.email = email
        x.password = password
        x.address = address
        x.address_two = addresstwo
        x.city = city
        x.state = state
        x.country = country
        x.zip_code = zip_code
        BS.create(username)
        x.save()

        return Response(user.data, status=status.HTTP_201_CREATED)
    
        res = requests.post(f"{authUrl}auth/v1/register", data ={'key':'value'})
        return Response({"message": res.json()}, status=status.HTTP_200_OK)