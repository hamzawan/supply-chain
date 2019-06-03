from django.db import models
from inventory.models import Add_item
import datetime


class ChartOfAccount(models.Model):
    account_title = models.CharField(max_length = 100, unique = True)
    parent_id = models.IntegerField()
    opening_balance = models.DecimalField(max_digits = 8, decimal_places = 2)
    phone_no = models.CharField(max_length = 100)
    email_address = models.CharField(max_length = 100)
    ntn = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 200)
    remarks = models.CharField(max_length = 100)


class PurchaseHeader(models.Model):
    purchase_no = models.CharField(max_length = 100, unique = True)
    date = models.DateField(default = datetime.date.today)
    footer_description = models.TextField()
    payment_method = models.CharField(max_length = 100)
    account_id = models.ForeignKey(ChartOfAccount, models.SET_NULL,blank=True,null=True,)


class PurchaseDetail(models.Model):
    item_id = models.ForeignKey(Add_item, models.SET_NULL, blank=True, null=True)
    item_description = models.TextField()
    width = models.DecimalField(max_digits = 8, decimal_places = 2)
    height = models.DecimalField(max_digits = 8, decimal_places = 2)
    quantity = models.DecimalField(max_digits = 8, decimal_places = 2)
    square_fit = models.CharField(max_length = 100)
    rate = models.DecimalField(max_digits = 8, decimal_places = 2)
    purchase_id = models.ForeignKey(PurchaseHeader, on_delete = models.CASCADE)



class SaleHeader(models.Model):
    sale_no = models.CharField(max_length = 100, unique = True)
    date = models.DateField(default = datetime.date.today)
    footer_description = models.TextField()
    payment_method = models.CharField(max_length = 100)
    account_id = models.ForeignKey(ChartOfAccount, models.SET_NULL,blank=True,null=True,)


class SaleDetail(models.Model):
    item_id = models.ForeignKey(Add_item, models.SET_NULL, blank=True, null=True)
    item_description = models.TextField()
    width = models.DecimalField(max_digits = 8, decimal_places = 2)
    height = models.DecimalField(max_digits = 8, decimal_places = 2)
    quantity = models.DecimalField(max_digits = 8, decimal_places = 2)
    square_fit = models.CharField(max_length = 100)
    rate = models.DecimalField(max_digits = 8, decimal_places = 2)
    sale_id = models.ForeignKey(SaleHeader, on_delete = models.CASCADE)


class Company_info(models.Model):
    company_name = models.CharField(max_length = 100)
    company_address = models.TextField()
    company_logo = models.TextField()
    phone_no = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    website = models.CharField(max_length = 100)
