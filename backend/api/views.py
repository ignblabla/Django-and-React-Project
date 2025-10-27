from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #Define el conjunto de objetos de base de datos (QuerySet) que esta vista está destinada a manejar.
    serializer_class = UserSerializer #Especifica qué clase de serializador debe usar la vista para procesar los datos entrantes.
    permission_classes = [AllowAny] #Controla quién puede acceder a esta vista.