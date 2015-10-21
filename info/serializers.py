from rest_framework import serializers
from info.models import Detail


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('id', 'name', 'create_dt')




