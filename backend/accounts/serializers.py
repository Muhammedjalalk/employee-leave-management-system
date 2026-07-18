from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model
class RegisterSerializers(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.EmailField()

    password=serializers.CharField(
        write_only=True,
        min_length=8   
    )

    class meta:
        model=User
        field=['id','username','email','password']
        