from rest_framework import serializers
from account.models import Users


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'mobile', 'email', 'password', 'login_type')
