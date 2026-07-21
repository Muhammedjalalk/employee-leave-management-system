from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class RegisterSerializers(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.EmailField()

    password=serializers.CharField(
        write_only=True,
        min_length=8   
    )

    class meta:
        model=User
        field=['id','username','email','password'.'role']

    def create(self,validate_data):
        User=User.objects.create_user(
            username=validate_data['username'],
            password=validate_data['password'],
            email=validate_data.get['email'],
            role=validate_data.get('role','employee')
        )
        return User
    
class CustomTokenObtainObjectSerilizer(TokenObtainPairSerializer):
    @classmethod

    def get_token(cls, user):
        token=super().get_token(user)
        token['username']=user.name
        token['role']=user.role
        return token
        