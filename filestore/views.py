# Django imports
from django.shortcuts import render

# DRF imports
from rest_framework import generics

from .serializers import StoreSerializer, StoreProductsSerializer

from store_client import CobiroStoreAPI

store_api = CobiroStoreAPI('english_shops.json')


class ListStores(generics.ListAPIView):

    queryset = store_api.get_stores()
    serializer_class = StoreSerializer

class ListStoreProducts(generics.ListAPIView):

    serializer_class = StoreProductsSerializer

    def get_queryset(self):
        store_name = " ".join(self.kwargs["store_slug"].split("-"))
        queryset = store_api.get_store_products(store_name)
        return queryset
