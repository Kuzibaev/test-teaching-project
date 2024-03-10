from rest_framework import generics

from api.v1.products.serializers import ProductSerializer
from products.models import Product


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
