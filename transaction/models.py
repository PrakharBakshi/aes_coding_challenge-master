from django.db import models
from datetime import datetime


# Masters required in transaction models
class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=10)
    def __str__(self):
        return self.short_name


class DepartmentMaster(models.Model):
    depname = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.depname


class CompanyLedgerMaster(models.Model):
    comname = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.comname


class ArticleMaster(models.Model):
    articlename = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)
    def __str__(self):
        return self.articlename


class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)
    def __str__(self):
        return self.name

CHOICES = (
    ("1", "PENDING"),
    ("2", "COMPLETED"),
    ("3", "CLOSE"),
)

class Transaction(models.Model):
    comname=models.ForeignKey(CompanyLedgerMaster,verbose_name="CompanyLedgerName",default=1,on_delete=models.SET_DEFAULT)
    short_name=models.ForeignKey(BranchMaster,verbose_name="BranchName",default=1,on_delete=models.SET_DEFAULT)
    depname=models.ForeignKey(DepartmentMaster,verbose_name="departmentName",default=1,on_delete=models.SET_DEFAULT)
    transaction_number=models.CharField(max_length=10,unique=True,null=True)
    transaction_status=models.CharField(max_length = 20,choices=CHOICES,default = '1')
    Transaction_id=models.PositiveIntegerField(null=True)
    Remark=models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not Transaction.objects.count()==0:
            today = datetime.today()
            last_transaction=Transaction.objects.last()
            COUNT=last_transaction.transaction_number[4:]
            last_transaction_year=last_transaction.transaction_number[-5:]
            current_year=today.year
            if int(current_year)==int(last_transaction_year.replace("/","")):
                COUNT=COUNT.replace(last_transaction_year,"")
                COUNT=int(COUNT)+1
                self.transaction_number = "TRN/"+str(COUNT)+"/"+str(current_year)
            else:
                self.transaction_number = "TRN/"+str(1)+"/"+str(current_year)
        super(Transaction,self).save(*args, **kwargs)


class TransactionDetail(models.Model):
    articlename=models.ForeignKey(ArticleMaster,verbose_name="ArticleName",default=1,on_delete=models.SET_DEFAULT)
    name=models.ForeignKey(ColorMaster,verbose_name="Colorname",default=1,on_delete=models.SET_DEFAULT)
    required_date=models.DateTimeField(auto_now_add=True)
    quantity=models.DecimalField(max_digits=5, decimal_places=2)
    Rate_per_unit=models.IntegerField()
    TransactionDetail_id=models.PositiveIntegerField(null=True)
    Unit=models.CharField(max_length = 20, choices=(("1", "KG"),("2", "METRE"),) , default = '1')

class InventoryItem(models.Model):
    articlename=models.ForeignKey(ArticleMaster,verbose_name="ArticleName",default=1,on_delete=models.SET_DEFAULT)
    name=models.ForeignKey(ColorMaster,verbose_name="Colorname",default=1,on_delete=models.SET_DEFAULT)
    comname=models.ForeignKey(CompanyLedgerMaster,verbose_name="CompanyLedgerName",default=1,on_delete=models.SET_DEFAULT)
    grossquantity=models.DecimalField(max_digits=5, decimal_places=2)
    netquantity=models.DecimalField(max_digits=5, decimal_places=2)
    Unit=models.CharField(max_length = 20, choices=(("1", "KG"),("2", "METRE"),) , default = '1')
    InventoryItem_id=models.PositiveIntegerField(null=True)







# Create your models here.
