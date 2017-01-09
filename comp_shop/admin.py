from django.contrib import admin
from comp_shop.models import Computer

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'brand', 'comp_pic')
    search_fields = ('serial_num', 'brand')


admin.site.register(Computer, ComputerAdmin)

# Register your models here.
