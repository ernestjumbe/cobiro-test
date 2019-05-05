from rest_framework import serializers

class StoreSerializer(serializers.Serializer):

    store_name = serializers.CharField()

class StoreProductsSerializer(serializers.Serializer):

    title = serializers.CharField()
    link = serializers.CharField()
    description = serializers.CharField()
    image_link = serializers.CharField()
