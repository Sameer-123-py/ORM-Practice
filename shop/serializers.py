
from rest_framework import serializers
from .models import Customer, CustomerProfile, Product, Order, OrderItem

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['phone', 'city']

class CustomerSerializer(serializers.ModelSerializer):
    profile = CustomerProfileSerializer(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'join_date', 'is_premium', 'profile']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'stock_quantity', 'is_active']

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')
    
    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_name', 'order_date', 'total_amount', 'status', 'items']