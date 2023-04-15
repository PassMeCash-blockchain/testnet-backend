
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
import uuid

User=get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=10,write_only=True)
    phone_number=serializers.IntegerField()
    class Meta:
        model=UserDetail
        fields=("phone_number","password")

    # def validate(self,data):
    #     phone=data.get('phone_number')
    #     if UserDetail.objects.filter(phone_number=phone).exists():
    #         serializers.ValidationError({'error':'phone number already in use'})
    #     return data

    def create(self,validated_data):
        table_user=None
        if not UserDetail.objects.filter(phone_number=self.initial_data['phone_number']).exists():
            table_user=User.objects.create_user(
            username=str(uuid.uuid4()),
            password=self.initial_data['password']
        )
        else:
            serializers.ValidationError({'error':'phone number already used'})
        if table_user is not None:
            details=UserDetail.objects.create(
            phone_number=self.initial_data['phone_number'],
            user=table_user
            )
            details.save()
            return details.user
        else:
            return {'Error':"registration failed"}
