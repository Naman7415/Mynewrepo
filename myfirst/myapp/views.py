from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import TenantSerializer,TenantDataSerializer
from rest_framework.throttling import UserRateThrottle
from rest_framework import permissions

class Tenant1ModelView(APIView):
    def get(self, request):
        queryset = Tenant1Model.objects.all()
        serializer = TenantSerializer(queryset, many=True)
        return Response(serializer.data)





class MyThrottle(UserRateThrottle):
    rate = '10/day'
    
class Tenant2ModelView(APIView):
    throttle_classes = [MyThrottle]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        queryset = Tenant2Model.objects.all()
        serializer = TenantDataSerializer(queryset, many=True)
        return Response(serializer.data)



