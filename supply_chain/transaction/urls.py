from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='transaction-home'),

    path('purchase/', views.purchase, name='purchase'),
    path('purchase_return/', views.purchase_return, name='purchase-return'),
    path('sale/', views.sale, name='sale'),
    path('sale_return/', views.sale_return, name='sale-return'),
]
