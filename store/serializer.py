from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','profile_photo','email')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields =('id','user','category','name', 'description','price')

