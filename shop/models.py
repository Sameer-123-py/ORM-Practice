# shop/models.py
from django.db import models
from django.utils import timezone
from datetime import timedelta

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class InvoiceQuerySet(models.QuerySet):
    def paid(self):
        return self.filter(is_paid=True)

    def last_30_days(self):
        return self.filter(paid_at__gte=timezone.now() - timedelta(days=30))

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)

    objects = InvoiceQuerySet.as_manager()  # ✅ chainable queries

    def __str__(self):
        return f"{self.customer.name} - {self.amount}"
