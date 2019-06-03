from django.shortcuts import render
from django.http import JsonResponse
from .models import Add_item
import json



def add_item(request):
    get_item_code = Add_item.objects.last()
    if get_item_code:
        get_item_code = get_item_code.item_code
        serial_no = get_item_code[8:]
        serial_no = int(serial_no) + 1
    else:
        inc = 1
        serial_no = int('101')
    item_description = request.POST.get("item_description")
    unit = request.POST.get("unit")
    type = request.POST.get("type")
    size = request.POST.get("size")
    opening_stock = request.POST.get("opening_stock")
    print(type)
    if item_description and type and size:
        return JsonResponse({"item_description":item_description,"unit":unit,"type":type,"size":size,"opening_stock":opening_stock})
    if request.method == "POST":
        items = json.loads(request.POST.get('items'))
        for value in items:
            type = value["type"][:3]
            size = value["size"][:3]
            item_code = type+"-"+size+"-"+str(serial_no)
            new_products = Add_item(item_code = item_code, item_description = value["item_description"], unit = value["unit"] ,opening_stock = value["opening_stock"])
            new_products.save()
            return JsonResponse({"success":"success"})
    return render(request,'inventory/add_item.html')


def stock(request):
    return render(request,'inventory/stock.html')
