from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from api.v1.products.serializers import ProductSerializer
from products.models import Product


class ProductListView(GenericAPIView):
    def get(self, request):  # noqa
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"result": serializer.data})
