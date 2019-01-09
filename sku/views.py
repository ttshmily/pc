from django.shortcuts import render
from sku.models import SKU
from sku.serializer import SKUSerializer
from rest_framework.mixins import ListModelMixin


# Create your views here.
class SKU(ListModelMixin):
    pass
    serializer_class = SKUSerializer
    queryset = SKU.objects.all()

    def get(self, request):
        return self.list(request)

