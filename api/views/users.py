from django.http import response
from rest_framework import serializers
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from jwt_project.api.serializers.serializers import (
    UserSerializer,
    UserInfoSerializer
)
from jwt_project.db.models.library import User
from django.contrib.auth import authenticate
from rest_framework import exceptions
import datetime
from rest_framework import status
from django.conf import settings
import jwt
from rest_framework.views import APIView
from django.contrib.auth import get_user_model


def generate_access_token(user):
    print(user[0]["id"])
    print(user)
    access_token_payload = {
        "user_id": user[0]["id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10080),
        "iat": datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY, algorithm="HS256"
    )
    return access_token

def generate_refresh_token(user):
    refresh_token_payload = {
        "user_id": user[0]["id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
        "iat": datetime.datetime.utcnow(),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm="HS256"
    )

    return refresh_token


class UserView(APIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        if (email is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                "please provide email or phone number to signup"
            )
        if User.objects.filter(email=email).exists():
            raise exceptions.AuthenticationFailed("user already exists")

        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def get(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        user= User.objects.filter(email=email,password=password)
        if not user:
            return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
        serialized_user=UserInfoSerializer(user, many=True).data
        response=Response()
        access_token = generate_access_token(serialized_user)
        refresh_token = generate_refresh_token(serialized_user)
        response.set_cookie(key="refreshtoken", value=refresh_token, httponly=True)
        response.data = {
            "access_token": access_token,
            "user": serialized_user,
        }
        return response


class UserInfoView(APIView):
    def get(self, request):
        response_payload = {
            "id": request.user.id,
            "email": request.user.email,
            "username": request.user.username,
        }
        return Response(response_payload)

