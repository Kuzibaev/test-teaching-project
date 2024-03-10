from django.contrib import admin

from products.models import Product, ProductMaterial, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass
