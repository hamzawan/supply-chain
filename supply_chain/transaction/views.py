from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'transaction/index.html')


def purchase(request):
    return render(request, 'transaction/purchase.html')


def purchase_return(request):
    return render(request, 'transaction/purchase_return.html')


def purchase_return_summary(request):
    return render(request, 'transaction/purchase_return_summary.html')


def sale(request):
    return render(request, 'transaction/sale.html')


def sale_return(request):
    return render(request, 'transaction/sale_return.html')


def sale_return_summary(request):
    return render(request, 'transaction/sale_return_summary.html')