from django.urls import path
from .views import (
    ProductListApiView,
    TypeListApiView,
    ClientListApiView
)

urlpatterns = [
    path('api/products/', ProductListApiView.as_view(), name="product_list"),
    # path('api/products/<int:type>', ProductListApiView.as_view(), name="product_list_by_type"),
    path('api/product_types', TypeListApiView.as_view(), name="product_type"),
    path('api/clients', ClientListApiView.as_view(), name="client"),
]