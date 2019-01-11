from rest_framework import serializers
from curriculum.models import Curricula


class CurriculumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curricula
        fields = ('pk', 'title', 'desc', 'duration', 'status', 'coach')


class FixedCoachTimeSerializer(serializers.ModelSerializer):

    coach_name = serializers.CharField(source='coach.nickname')
    coach_id = serializers.IntegerField(source='coach.user_id')
    coach_avatar = serializers.ImageField(source='coach.avatar')

    class Meta:
        model = Curricula
        fields = ('title', 'desc', 'duration', 'status', 'coach_id', 'coach_name', 'coach_avatar')
        # fields = ('pk', 'title', 'desc', 'duration', 'status')

    def get_coach_name(self, obj):
        return 'tt'
