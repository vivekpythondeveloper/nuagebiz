from rest_framework import serializers

from .models import SearchApi


class SearchApiSerializer(serializers.ModelSerializer):

    class Meta:
        model                       = SearchApi
        fields                      = ['product_name','image_url','price']