from curriculum.models import Curricula
from curriculum.serializers import CurriculumSerializer, FixedCoachTimeSerializer
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse


# Create your views here.
class CurriculumViewSet(ModelViewSet):

    serializer_class = CurriculumSerializer
    queryset = Curricula.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def create(self, request, *args, **kwargs):
    #     pass

    # def list(self, request, *args, **kwargs):
    #     pass


class FixedCoachTimeCurriculum(ModelViewSet):

    def get_serializer_class(self):
        return FixedCoachTimeSerializer

    def get_queryset(self):
        return Curricula.objects.all()

    def list(self, request, *args, **kwargs):
        ser = self.get_serializer_class()
        q1 = self.get_queryset().filter(coach=1)
        return JsonResponse(ser(q1, many=True).data, safe=False)
