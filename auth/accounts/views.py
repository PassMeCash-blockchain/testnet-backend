from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserDetail
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *
import json

# Create your views here.

class RegisterView(APIView):

    def get(self,request):
        qs=UserDetail.objects.all()
        serializer=UserCreateSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=UserCreateSerializer(data=(dict(request.data)))
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'details':"user created sucessfully"})


