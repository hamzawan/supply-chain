from django.shortcuts import render
from inventory.models import Add_item
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import ChartOfAccount, PurchaseHeader, PurchaseDetail, SaleHeader, SaleDetail, Company_info
import datetime, json
from .utils import render_to_pdf
from django.template.loader import get_template


def home(request):
    return render(request, 'transaction/index.html')


def purchase(request):
    all_purchases = PurchaseHeader.objects.all()
    return render(request, 'transaction/purchase.html',{'all_purchases':all_purchases})


def new_purchase(request):
    all_item_code =  Add_item.objects.all()
    all_accounts = ChartOfAccount.objects.all()
    item_code_purchase = request.POST.get('item_code_purchase',False)
    get_last_purchase_no = PurchaseHeader.objects.last()
    if get_last_purchase_no:
        get_last_purchase_no = get_last_purchase_no.purchase_no
        get_last_purchase_no = get_last_purchase_no[-3:]
        num = int(get_last_purchase_no)
        num = num + 1
        get_last_purchase_no = 'PUR/' + str(num)
    else:
        get_last_purchase_no = 'PUR/101'
    if item_code_purchase:
        items = Add_item.objects.filter(item_code = item_code_purchase)
        row = serializers.serialize('json',items)
        return JsonResponse({"row":row})
    if request.method == "POST":
        purchase_id = request.POST.get('purchase_id',False)
        supplier = request.POST.get('supplier',False)
        payment_method = request.POST.get('payment_method',False)
        footer_desc = request.POST.get('footer_desc',False)
        account_id = ChartOfAccount.objects.get(account_title = supplier)
        date = datetime.date.today()

        purchase_header = PurchaseHeader(purchase_no = purchase_id, date = date, footer_description = footer_desc, payment_method = payment_method, account_id = account_id )

        items = json.loads(request.POST.get('items'))
        purchase_header.save()
        header_id = PurchaseHeader.objects.get(purchase_no = purchase_id)
        for value in items:
            item_id = Add_item.objects.get(item_code = value["item_code"])
            purchase_detail = PurchaseDetail(item_id = item_id, item_description = value["description"],width = value["width"],height = value["height"],quantity = value["qty"], square_fit = 0.00, rate = value["rate"], purchase_id = header_id)
            purchase_detail.save()
        #     quantity = float(value["quantity"])
        #     price =  float((value["price"]))
        #     sales_tax = float(value["sales_tax"])
        #     amount = (((quantity * price) * sales_tax) / 100)
        #     amount = ((quantity * price ) + amount)
        #     item_amount = item_amount + amount
        # item_amount = item_amount + float(cartage_amount) + float(additional_tax)
        # tax = ((item_amount * float(withholding_tax)) / 100)
        # total_amount = tax + item_amount
        # tran = Transactions(refrence_id = header_id, refrence_date = date, account_id = account_id, tran_type = )
        return JsonResponse({'result':'success'})
    return render(request, 'transaction/new_purchase.html',{'all_item_code':all_item_code,"all_accounts":all_accounts,"get_last_purchase_no":get_last_purchase_no})


def purchase_return(request):
    return render(request, 'transaction/purchase_return.html')


def purchase_return_summary(request):
    return render(request, 'transaction/purchase_return_summary.html')


def sale(request):
    all_sale = SaleHeader.objects.all()
    return render(request, 'transaction/sale.html',{"all_sale":all_sale})

def new_sale(request):
    all_item_code =  Add_item.objects.all()
    all_accounts = ChartOfAccount.objects.all()
    item_code_purchase = request.POST.get('item_code_purchase',False)
    get_last_sale_no = SaleHeader.objects.last()
    if get_last_sale_no:
        get_last_sale_no = get_last_sale_no.sale_no
        get_last_sale_no = get_last_sale_no[-3:]
        num = int(get_last_sale_no)
        num = num + 1
        get_last_sale_no = 'SALE/' + str(num)
    else:
        get_last_sale_no = 'SALE/101'
    if item_code_purchase:
        items = Add_item.objects.filter(item_code = item_code_purchase)
        row = serializers.serialize('json',items)
        return JsonResponse({"row":row})
    if request.method == "POST":
        sale_id = request.POST.get('sale_id',False)
        customer = request.POST.get('customer',False)
        payment_method = request.POST.get('payment_method',False)
        footer_desc = request.POST.get('footer_desc',False)
        account_id = ChartOfAccount.objects.get(account_title = customer)
        date = datetime.date.today()

        sale_header = SaleHeader(sale_no = sale_id, date = date, footer_description = footer_desc, payment_method = payment_method, account_id = account_id )

        items = json.loads(request.POST.get('items'))
        sale_header.save()
        header_id = SaleHeader.objects.get(sale_no = sale_id)
        for value in items:
            item_id = Add_item.objects.get(item_code = value["item_code"])
            sale_detail = SaleDetail(item_id = item_id, item_description = value["description"],quantity = value["qty"], price = value["rate"], sale_id = header_id)
            sale_detail.save()
        #     quantity = float(value["quantity"])
        #     price =  float((value["price"]))
        #     sales_tax = float(value["sales_tax"])
        #     amount = (((quantity * price) * sales_tax) / 100)
        #     amount = ((quantity * price ) + amount)
        #     item_amount = item_amount + amount
        # item_amount = item_amount + float(cartage_amount) + float(additional_tax)
        # tax = ((item_amount * float(withholding_tax)) / 100)
        # total_amount = tax + item_amount
        # tran = Transactions(refrence_id = header_id, refrence_date = date, account_id = account_id, tran_type = )
        return JsonResponse({'result':'success'})
    return render(request, 'transaction/new_sale.html',{'all_item_code':all_item_code,"all_accounts":all_accounts,"get_last_sale_no":get_last_sale_no})


def chart_of_account(request):
    if request.method == 'POST':
        account_title = request.POST.get('account_title')
        account_type = request.POST.get('account_type')
        opening_balance = request.POST.get('opening_balance')
        phone_no = request.POST.get('phone_no')
        email_address = request.POST.get('email_address')
        ntn = request.POST.get('ntn')
        address = request.POST.get('address')
        remarks = request.POST.get('remarks')
        if opening_balance is "":
            opening_balance = 0
        coa = ChartOfAccount(account_title = account_title, parent_id = account_type, opening_balance = opening_balance, phone_no = phone_no, email_address = email_address, ntn = ntn, Address = address, remarks = remarks)
        coa.save()
    customer_accounts = ChartOfAccount.objects.filter(parent_id = 1)
    supplier_accounts = ChartOfAccount.objects.filter(parent_id = 2)
    return render(request, 'transaction/chart_of_account.html',{'customer_accounts':customer_accounts, 'supplier_accounts':supplier_accounts})


def sale_return(request):
    return render(request, 'transaction/sale_return.html')


def sale_return_summary(request):
    return render(request, 'transaction/sale_return_summary.html')


def print_purchase(request,pk):
    lines = 0
    total_amount = 0
    total_quantity = 0
    total_square_fit = 0
    square_fit = 0
    header = PurchaseHeader.objects.filter(id = pk).first()
    detail = PurchaseDetail.objects.filter(purchase_id = pk).all()
    image = Company_info.objects.first()
    for value in detail:
        lines = lines + len(value.item_description.split('\n'))
        square_fit = float(value.width * value.height)
        gross = square_fit * float(value.rate)
        amount = gross * float(value.quantity)
        total_amount = total_amount + amount
        total_quantity = (total_quantity + value.quantity)
        square_fit = value.height * value.width
        total_square_fit = total_square_fit + square_fit
    lines = lines + len(detail) + len(detail)
    total_lines = 36 - lines
    pdf = render_to_pdf('transaction/purchase_pdf.html', {'header':header, 'detail':detail,'image':image, 'total_lines':12, 'total_amount':total_amount, 'total_quantity':total_quantity,'total_square_fit':total_square_fit})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Purchase_%s.pdf" %(header.purchase_no)
        content = "inline; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


def print_sale(request,pk):
    lines = 0
    total_amount = 0
    total_quantity = 0
    total_square_fit = 0
    square_fit = 0
    header = SaleHeader.objects.filter(id = pk).first()
    detail = SaleDetail.objects.filter(sale_id = pk).all()
    image = Company_info.objects.first()
    for value in detail:
        lines = lines + len(value.item_description.split('\n'))
        square_fit = float(value.width * value.height)
        gross = square_fit * float(value.rate)
        amount = gross * float(value.quantity)
        total_amount = total_amount + amount
        total_quantity = (total_quantity + value.quantity)
        square_fit = value.height * value.width
        total_square_fit = total_square_fit + square_fit
    lines = lines + len(detail) + len(detail)
    total_lines = 36 - lines
    pdf = render_to_pdf('transaction/sale_pdf.html', {'header':header, 'detail':detail,'image':image, 'total_lines':12, 'total_amount':total_amount, 'total_quantity':total_quantity,'total_square_fit':total_square_fit})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Sale_%s.pdf" %(header.sale_no)
        content = "inline; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")
