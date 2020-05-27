from rest_framework import serializers
from .models import HumedadAire

class HumedadAireSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumedadAire
        fields = ('id','type', 'value', 'latitude', 'longitude', 'terrain')