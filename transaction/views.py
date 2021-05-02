from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import BranchMaster,DepartmentMaster,CompanyLedgerMaster,ArticleMaster,ColorMaster
from .models import Transaction,TransactionDetail,InventoryItem
from .serializers import TransactionSerializer,DetailSerializer,InventorySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class TransactionAPIView(APIView):
    def get(self,request):
        trans=Transaction.objects.all()
        serializer=TransactionSerializer(trans,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=TransactionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TransactionDetails(APIView):
    def get_object(self,id):
        try:
            return Transaction.objects.get(id=id)
        except Transaction.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_NOT_FOUND)

    def get(self,request,id):
        trans=self.get_object(id)
        serializer=TransactionSerializer(trans)
        return Response(serializer.data)

    def put(self,request,id):
        tran=self.get_object(id)
        serializer=TransactionSerializer(tran)
        serial=DetailSerializer(data=request.data)
        if serial.is_valid():
                serial.save()
                return Response(serial.data)
                ser=InventorySerializer(data=request.data)
                if ser.is_valid():
                    ser.save()
                    return Response(ser.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        transaction=self.get_object(id)
        details=TransactionDetail.objects.get(id=id)
        transaction.delete()
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class showall(APIView):
    def get_object(self,id):
        try:
            return Transaction.objects.get(id=id)
        except Transaction.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_NOT_FOUND)
    def get(self,request,id):
        trans=self.get_object(id)
        trans1=TransactionDetail.objects.get(TransactionDetail_id=trans.Transaction_id)
        trans2=InventoryItem.objects.get(InventoryItem_id=trans.Transaction_id)
        serializer=TransactionSerializer(trans)
        serializer1=DetailSerializer(trans1)
        serializer2=InventorySerializer(trans2)
        listq=[serializer.data,serializer1.data,serializer2.data]
        return Response(listq)
