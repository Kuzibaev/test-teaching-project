from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255, null=True, blank=True)

    def __repr__(self):
        return f'Product: {self.product_name}'

    def __str__(self):
        return self.__repr__()


class Material(models.Model):
    material_name = models.CharField(max_length=255)


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='product_materials')
    quantity = models.PositiveIntegerField()


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Warehouse: {self.id}'

    def __repr__(self):
        return self.__repr__()
