from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
# create form for the admin panel, with order details and 
# a record of each item included in that order.

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    
admin.site.register(Order, OrderAdmin)