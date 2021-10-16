from django.contrib import admin

from .models import*

# Register your models here.
admin.site.register(Product)
admin.site.register(Signup)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Sell)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
