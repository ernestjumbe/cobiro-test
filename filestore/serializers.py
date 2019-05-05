from rest_framework import serializers

class StoreSerializer(serializers.Serializer):

    store_name = serializers.CharField()
