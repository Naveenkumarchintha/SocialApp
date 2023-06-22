from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegistrationAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if username and password and email:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Please provide username, password, and email.'}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)

                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Please provide username and password.'}, status=status.HTTP_400_BAD_REQUEST)
