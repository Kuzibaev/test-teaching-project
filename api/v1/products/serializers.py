from rest_framework import serializers

from products.models import Product, ProductMaterial, Material, Warehouse


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


class ProductSerializer(serializers.ModelSerializer):
    product_materials = ProductMaterialSerializer(source='productmaterial_set', many=True, read_only=True)
    material_info = serializers.SerializerMethodField('get_material_info')

    class Meta:
        model = Product
        fields = ['product_name', 'product_qty', 'product_materials', 'material_info']

    def get_material_info(self, obj):
        material_info = {}
        for product_material in obj.productmaterial_set.all():
            material = product_material.material
            warehouse = product_material.warehouse
            if material.id not in material_info:
                material_info[material.id] = {
                    'material_name': material.material_name,
                    'qty': product_material.quantity,
                    'warehouse_id': warehouse.id,
                    'price': warehouse.price if warehouse.price else None
                }
            else:
                material_info[material.id]['qty'] += product_material.quantity
        return list(material_info.values())
