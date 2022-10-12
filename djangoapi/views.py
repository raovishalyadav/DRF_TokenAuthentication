from .models import something
from .serializers import serializers_something, serializers_user
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class ViewSet_something(viewsets.ModelViewSet):
    queryset = something.objects.all()
    serializer_class = serializers_something 
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

class ViewSet_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers_user