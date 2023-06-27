from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdsSerializer
from .models import Ads
from rest_framework import status
from .pagination import StandardResultSetPaginaton
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPublisherOrReadOnly
from rest_framework.parsers import MultiPartParser
from django.http import Http404
from django.db.models import Q
# Create your views here.
class AdsListView(APIView, StandardResultSetPaginaton):
    permission_classes = [IsPublisherOrReadOnly]
  
    serializer_class  = AdsSerializer
    def get(self, request):
        query = Ads.objects.filter(is_public=True)
        result = self.paginate_queryset(query, request)
        serializer = AdsSerializer(instance=result,many=True)
        return self.get_paginated_response(serializer.data)
        
class AdsCreateView(APIView):
    permission_classes = [IsAuthenticated,IsPublisherOrReadOnly]
    serializer_class = AdsSerializer
    parser_classes = [MultiPartParser,]

    def post(self,request):
        serializer = AdsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['publisher'] = self.request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdsDetailView(APIView):
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated, IsPublisherOrReadOnly]
    parser_classes = (MultiPartParser,)
    

    # def get_object(self,request):
    #     obj = get_object_or_404(Ads.objects.all(), id=self.kwargs['pk'])
    #     self.check_object_permissions(request, obj)
    #     return obj

    def get(self,request,pk):
        obj = Ads.objects.get(id=pk)
        serializer = AdsSerializer(instance=obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        obj = Ads.objects.get(id=pk)
        self.check_object_permissions(request, obj)
        serializer = AdsSerializer(instance=obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        obj = Ads.objects.get(id=pk)
        self.check_object_permissions(request, obj)
        obj.delete()
        return Response({'response':'Done'},status=status.HTTP_200_OK)
    

class AdsSearchView(APIView):
    serializer_class = AdsSerializer
    permission_classes = (IsPublisherOrReadOnly,)

    def get(self,request):
        q = request.GET.get('q')
        obj = Ads.objects.filter(Q(title=q) | Q(caption=q))
        reuslt = self.paginate_queryset(obj, request)
        serializer = AdsSerializer(instance=reuslt, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

    