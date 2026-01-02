from django.urls import path
from .views import invoices_api, customers_api

urlpatterns = [
    path('invoices/', invoices_api),
    path('customers/', customers_api),
]



