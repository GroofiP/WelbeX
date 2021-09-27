from rest_framework import viewsets

from mainapp.models import TableWebix
from api_v0.serializers import TableWebixModelSerializer


class TableWebixViewSet(viewsets.ModelViewSet):
    queryset = TableWebix.objects.all()
    serializer_class = TableWebixModelSerializer
