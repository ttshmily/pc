from rest_framework import serializers
from book.models import BookInformation


class BookInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInformation
        fields = ('url', 'book_title', 'book_cover', 'pub_date')

