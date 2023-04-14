from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password as vp
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth.models import User


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

    def create(self, validate_data):
        user = User.objects.create(
            username=validate_data['username'],
        )
        user.set_password(validate_data['password']),
        user.save()

        return user