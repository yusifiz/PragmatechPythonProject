from django.contrib import admin
from .models import Product,Tag
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name','color','product_tag','is_active')


admin.site.register(Tag)