from django.contrib import admin
from comp_shop.models import Computer, User, Order


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'brand', 'comp_pic')
    search_fields = ('serial_num', 'brand')

admin.site.register(Computer, ComputerAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')

admin.site.register(User, UserAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'user_id')
    list_filter = ['order_date']

admin.site.register(Order, OrderAdmin)
# Register your models here.
