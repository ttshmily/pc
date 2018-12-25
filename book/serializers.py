from django.contrib.auth.models import User, Group
from rest_framework import serializers
from book.models import BookInformation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BookInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookInformation
        fields = ('url', 'btitle', 'bpub_date', 'bcomment')

