from .models import BranchMaster,DepartmentMaster,CompanyLedgerMaster,ArticleMaster,ColorMaster
from .models import Transaction,TransactionDetail,InventoryItem
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransactionDetail
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryItem
        fields = '__all__'
