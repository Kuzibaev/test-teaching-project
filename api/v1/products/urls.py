from django.urls import path

from api.v1.products.views import ProductListAPIView

urlpatterns = [
    path('product-list/', ProductListAPIView.as_view(), name='product-list'),
]
