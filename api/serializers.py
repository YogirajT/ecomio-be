from rest_framework import serializers
from api.models import DestinationModel, SearchDataModel


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationModel
        fields = '__all__'

class SearchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchDataModel
        fields = '__all__'