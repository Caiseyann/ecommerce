from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','email')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields =('category','name', 'description','price')

