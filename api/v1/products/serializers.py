from rest_framework import serializers

from products.models import Product, ProductMaterial, Material, Warehouse


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name',)


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ProductMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMaterial
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = Warehouse
        fields = '__all__'
