# Django imports
from django.conf import settings
from django.shortcuts import render

# DRF imports
from rest_framework import generics

# Module imports
from .serializers import StoreSerializer, StoreProductsSerializer

# Thir party imports
from store_client import CobiroStoreAPI

store_api = CobiroStoreAPI(settings.DATA_SOURCE_FILE)


class ListStores(generics.ListCreateAPIView):

    queryset = store_api.get_stores()
    serializer_class = StoreSerializer

class ListStoreProducts(generics.ListCreateAPIView):

    serializer_class = StoreProductsSerializer

    def get_queryset(self):
        store_name = " ".join(self.kwargs["store_slug"].split("_"))
        queryset = store_api.get_store_products(store_name)
        return queryset

    def perform_create(self, serializer):
        store_name = " ".join(self.kwargs["store_slug"].split("_"))
        serializer.save(store_name)
