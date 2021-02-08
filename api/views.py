from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework import status

from accounts.models import User
from accounts.serializers import UserSerializer


class ListUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'



