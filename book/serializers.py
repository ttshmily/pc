from rest_framework import serializers
from book.models import BookInformation


class BookInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInformation
        fields = ('url', 'title', 'image')

