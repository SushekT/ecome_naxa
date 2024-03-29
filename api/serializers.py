from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'leather', 'polyster', 'Guarantee']
