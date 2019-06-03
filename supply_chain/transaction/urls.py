from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='transaction-home'),

    path('chart_of_account/', views.chart_of_account, name='chart-of-account'),

    path('purchase/', views.purchase, name='purchase'),
    path('purchase/new/', views.new_purchase, name='new-purchase'),
    path('purchase_return/', views.purchase_return, name='purchase-return'),
    path('purchase/print/<pk>', views.print_purchase, name='purchase-print'),

    path('sale/', views.sale, name='sale'),
    path('sale/new/', views.new_sale, name='new-sale'),
    path('sale_return/', views.sale_return, name='sale-return'),
    path('sale/print/<pk>', views.print_sale, name='sale-print'),
]
