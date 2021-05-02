from django.contrib import admin
from .models import BranchMaster,DepartmentMaster,CompanyLedgerMaster,ArticleMaster,ColorMaster
from .models import Transaction,TransactionDetail,InventoryItem

admin.site.register(BranchMaster)
admin.site.register(DepartmentMaster)
admin.site.register(CompanyLedgerMaster)
admin.site.register(ArticleMaster)
admin.site.register(ColorMaster)
admin.site.register(Transaction)
admin.site.register(TransactionDetail)
admin.site.register(InventoryItem)
