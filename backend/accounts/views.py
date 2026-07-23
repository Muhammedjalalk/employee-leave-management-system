from django.shortcuts import render

from  rest_framework import generics,permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializers,CustomTokenObtainObjectSerilizer

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializers
    permission_classes=[permissions.AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainObjectSerilizer
    permission_classes=[permissions.AllowAny]

    