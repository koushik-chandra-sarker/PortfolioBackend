import json

from django.contrib.postgres.aggregates import ArrayAgg
from django.core import serializers
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from author.models import User
from author.serializers import ChangePasswordSerializer, AuthorSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['type'] = "Bearer"
        # profile = json.loads(serializers.serialize('json', Profile.objects.filter(user=self.user)))
        user = json.loads(serializers.serialize('json', User.objects.filter(email=self.user)))
        try:
            # data['profile'] = profile[0]["fields"]
            data['profile']["author"] = user[0]['fields']
        except:
            data['profile'] = {}
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # # if using drf authtoken, create a new token
        # if hasattr(author, 'auth_token'):
        #     author.auth_token.delete()
        # token, created = Token.objects.get_or_create(author=author)
        # # return new token
        # return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'message': "Password update successful"}, status=status.HTTP_200_OK)
