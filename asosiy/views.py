from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status,filters
from rest_framework_simplejwt.authentication import JWTAuthentication
class SuvAPIView(ModelViewSet):

    queryset = Suv.objects.all()
    serializer_class = SuvSerializer
class MijozAPIView(ModelViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Mijoz.objects.all()
    serializer_class = MijozSerializer
class BuyurtmaAPIView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        buyurtmalar=Buyurtma.objects.all()
        serializer=BuyurtmaSerializer(buyurtmalar,many=True)
        return Response(serializer.data)
    def post(self,request):
        buyurtma=request.data
        serializer=BuyurtmaSerializer(data=buyurtma)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class AdminAPIView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,reuqest):
        admin=Admin.objects.all()
        serializer=AdminSerializer(admin,many=True)
        return Response(serializer.data)
class AdminDetailView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,son):
        admin = Admin.objects.get(id=son)
        serializer=AdminSerializer(admin)
        return Response(serializer.data)
class HaydovchiAPIView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,reuqest):
        haydovchi=Haydovchi.objects.all()
        serializer=HaydovchiSerializer(haydovchi,many=True)
        return Response(serializer.data)
class HaydovchiDetailView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,son):
        haydovchi = Haydovchi.objects.get(id=son)
        serializer=HaydovchiSerializer(haydovchi)
        return Response(serializer.data)