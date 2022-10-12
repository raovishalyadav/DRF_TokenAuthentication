from rest_framework import serializers
from .models import something
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class serializers_something(serializers.ModelSerializer):
    
    class Meta:
        model = something
        fields = ['id', 'first', 'second']
        #fields = '__all__'
    
class serializers_user(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        
        #to hide password on API call
        extra_kwargs = {
            'password':{
                'write_only':True,
                'required':True,
            }
        }
        
    #To hash the password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        #To automatically create token for the new user
        Token.objects.create(user=user)
        return user