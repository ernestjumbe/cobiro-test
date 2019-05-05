# Library imports
from rest_framework import serializers

# Module imports
from .models import Store, Product

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'

class StoreProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('store',)

    def save(self, store_id):
        store = Store.objects.get(id=store_id)
        Product.objects.create(
            store = store,
            title = self.validated_data['title'],
            link = self.validated_data['link'],
            description = self.validated_data['description'],
            image_link = self.validated_data['image_link'])
