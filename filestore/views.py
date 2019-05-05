# Django imports
from django.shortcuts import render

# DRF imports
from rest_framework import generics

from .serializers import StoreSerializer

from store_client import CobiroStoreAPI

store_api = CobiroStoreAPI('english_shops.json')


class ListStores(generics.ListAPIView):

    queryset = store_api.get_stores()
    serializer_class = StoreSerializer
