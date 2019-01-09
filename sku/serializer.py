from rest_framework.serializers import HyperlinkedModelSerializer
from sku.models import SKU


class SKUSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = SKU
        fields = ('url', 'book_title', 'book_cover', 'pub_date')
