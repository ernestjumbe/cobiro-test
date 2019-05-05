# Django imports
from django.shortcuts import render

# DRF imports
from rest_framework import generics

# Module imports
from .models import Store, Product
from .serializers import StoreSerializer, StoreProductsSerializer


class ListStores(generics.ListCreateAPIView):

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class ListStoreProducts(generics.ListCreateAPIView):

    serializer_class = StoreProductsSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(store=self.kwargs["store_id"])
        return queryset

    def perform_create(self, serializer):
        serializer.save(self.kwargs["store_id"])
