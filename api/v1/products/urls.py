from django.urls import path

from api.v1.products.views import ProductListView

urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product-list'),
]
