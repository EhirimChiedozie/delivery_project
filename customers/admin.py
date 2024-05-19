from django.contrib import admin
from .models import Customer, DeliveryOrder, OrderTracking
# Register your models here.

admin.site.register(Customer)
admin.site.register(DeliveryOrder)
admin.site.register(OrderTracking)