from .models import Uuuid
from rest_framework import serializers

class UuuidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uuuid
        fields = ['pub_date','uuid_char']