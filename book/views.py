from django.shortcuts import render
from django.contrib.auth.models import User, Group
from book.models import BookInformation
from rest_framework import viewsets
from book.serializers import UserSerializer, GroupSerializer, BookInformationSerializer
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the book index.")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BookInformationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BookInformation.objects.all()
    serializer_class = BookInformationSerializer
