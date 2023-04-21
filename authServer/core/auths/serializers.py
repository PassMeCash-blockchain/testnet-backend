from django.contrib.auth.password_validation import validate_password as vp
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (
    UserDetail as UD,
    Stage,
    LastLogin as LL
)
from .utils import *

import uuid, arrow, asyncio
from datetime import datetime

T = True
F = False


class Response(object):
    def success(x):
        data = {
            "message": x
        }
        data['status'] = 200
        return data

    def failed(x):
        data = {
            "message": x
        }
        data['status'] = 500
        return data

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        user = User(**data)
        password = data.get('password')
        try:
            vp(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password': serializer_errors['non_field_errors']}
            )

        return data

    async def init(data, user):
        UD.objects.create(user=userInfo(user.username),
                            phone_number=data['phone_number'])


    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
        )
        user.set_password(validate_data['password']),
        user.save()
        return user

    def personal(data):
        try:
            u = userInfo(data['uuid'])
            dob = data['dob']
            if '-' in dob:
                dob.replace('-', '/')
            
            if '-' not in dob and '/' not in dob:
                mssg = 'Invalid DOB format'
                return Response.failed(mssg)
            else:
                dob = datetime.strptime(dob, '%d/%m/%Y')
                User.objects.filter(username=u).update(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
                UD.objects.filter(user=u).update(dob=dob)
                Stage.objects.filter(user=u).update(stageTwo=T)
                mssg = 'done'
                return Response.success(mssg)

        except Exception as e:
            return Response.failed(str(e))


    def contact(data):
        try:
            u = userInfo(data['uuid'])
            UD.objects.filter(user=u).update(state=data['state'], lga=data['lga'], address=data['address'], addressAlt=data['addressAlt'])
            Stage.objects.filter(user=u).update(stageThree=T)
            mssg = 'done'
            return Response.success(mssg)

        except Exception as e:
            return Response.failed(str(e))
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

    # def read(user, r):
    #     getUser = AI.objects.get(username=userInfo(user).username)
    #     try:
    #         img = getUser.profile_pic.url
    #         img = URL(r)+img
    #     except Exception as e:
    #         img = None
    #     val = {
    #         "first_name": getUser.first_name,
    #         "last_name": getUser.last_name,
    #         "username": getUser.username,
    #         "email": getUser.email,
    #         "address": f"{getUser.address} {getUser.address_two} {getUser.city} {getUser.city} {getUser.state} {getUser.zip_code} {getUser.country}",
    #         "phone_number": getUser.phone_number,
    #         "profile_pic": img,
    #         "verified": getUser.verified,
    #     }

    #     class Response(object):
    #         data = val

    #     return Response

    def login(_u):
        U = userInfo(_u)
        try:
            getLastLogin = LL.objects.get_or_create(user=U)
            details = UD.objects.filter(user=U)

            for i in details:
                val = {
                    "phone_number": i.phone_number,
                    "dob": i.dob,
                    "state": i.state,
                    "lga": i.lga,
                    "address": i.address,
                    "address_alt": i.addressAlt,
                    "is_verified": T
                }
            res = {
                "last_login": getLastLogin[0].lastlogin,
                "registration_stage": getRegStage(_u),
                "user_details": val
            }

            return Response.success(res)
        except Exception as e:
            return Response.failed(str(e))

    def lastlogin(user):
        U = userInfo(user)
        try:
            LL.objects.filter(user=U).update(lastlogin=myTime().datetime)
            return Response.success('done')
        except Exception as e:
            LL.objects.create(user=U, lastlogin=myTime().datetime)
            return Response.success('done')

    

# class UserCreateSerializer(serializers.ModelSerializer):
