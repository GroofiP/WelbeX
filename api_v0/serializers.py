from rest_framework.serializers import ModelSerializer

from mainapp.models import TableWebix


class TableWebixModelSerializer(ModelSerializer):
    class Meta:
        model = TableWebix
        fields = "__all__"


