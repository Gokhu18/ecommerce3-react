from django.urls import path
from .views import *

urlpatterns = [
    path('user-id/', UserIDView.as_view(), name='user-id'),
    path('products/', ItemListView.as_view(), name='product-list'),
    # No item slug parameters because they are included in request.data
    path('products/<pk>/', ItemDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('order-summary/', OrderDetailView.as_view(), name='order-summary'),
    path('checkout/', PaymentView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('addresses/', AddressListView.as_view(), name='address-list'),
    path('addresses/create/', AddressCreateView.as_view(), name='address-create'),
    path('countries/', CountryListView.as_view(), name='country-list'),
]
