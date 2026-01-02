from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Invoice
from django.db.models import Sum, OuterRef, Subquery

# Invoices API (select_related)
@api_view(['GET'])
def invoices_api(request):
    qs = Invoice.objects.paid().last_30_days().select_related('customer')
    return Response([
        {"customer": inv.customer.name, "amount": inv.amount, "paid_at": inv.paid_at}
        for inv in qs
    ])

# Customers API (prefetch_related + annotate + subquery)
@api_view(['GET'])
def customers_api(request):
    total_paid_subquery = Invoice.objects.filter(
        customer=OuterRef('pk'),
        is_paid=True
    ).values('customer').annotate(total=Sum('amount')).values('total')

    qs = Customer.objects.prefetch_related('invoices').annotate(
        total_paid=Subquery(total_paid_subquery)
    )

    return Response([
        {"customer": c.name, "total_paid": c.total_paid or 0}
        for c in qs
    ])
