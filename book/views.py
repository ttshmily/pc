from rest_framework import viewsets
from rest_framework.views import APIView
from book.models import BookInformation
from book.serializers import BookInformationSerializer
from django.http import HttpResponse, JsonResponse
from account.authentication import Authentication
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the book index.")


class BookInformationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = []
    queryset = BookInformation.objects.all()
    serializer_class = BookInformationSerializer


class BookView(APIView):

    def get(self, request):
        # request.user
        # request.auth
        ret = {'code': 0, 'msg': 'success'}
        return JsonResponse(ret)




