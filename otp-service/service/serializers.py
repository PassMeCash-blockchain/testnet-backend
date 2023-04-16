from rest_framework import serializers
from .models import *

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model=phoneModel
        fields='__all__'
