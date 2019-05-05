from rest_framework import serializers

from store_client import CobiroStoreAPI

store_api = CobiroStoreAPI('english_shops.json')

class StoreSerializer(serializers.Serializer):

    store_name = serializers.CharField()

class StoreProductsSerializer(serializers.Serializer):

    title = serializers.CharField()
    link = serializers.CharField()
    description = serializers.CharField()
    image_link = serializers.CharField()

    def save(self, store_name):

        product = {
            'title': self.validated_data['title'],
            'link': self.validated_data['link'],
            'description': self.validated_data['description'],
            'image_link': self.validated_data['image_link']
        }

        store_api.create_product(store_name, product)
