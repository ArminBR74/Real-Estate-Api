from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

class UserView(APIView):
    serializer_class = [UserSerializer]
    '''
    GET Method shows you profile of users

    '''
    def get(self,request):
        user = request.user
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''
    PUT Method let you Update your account details
    '''
    def put(self,request):
        user = request.user
        #instance is needed
        serializer = UserSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)