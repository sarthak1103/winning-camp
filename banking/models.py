from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=122, null=True, default=None)
    email = models.EmailField()
    account_no = models.CharField(max_length=122,null=True,blank=True)
    balance = models.IntegerField(null=True,blank=True)
    class meta:
        db_table="customer"
        fields= ["name", "email", "account_no", "balance"]
class transfer(models.Model):
    payer=models.IntegerField(null=True,blank=True)
    payee=models.IntegerField(null=True,blank=True)
    amount=models.IntegerField(null=True,blank=True)
    class meta:
        db_table="transfer"
        fields=['payer','payee','amount']