from rest_framework import serializers
from .models import State, County, Town

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name']

class CountySerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = County
        fields = ['name', 'state']

class TownSerializer(serializers.ModelSerializer):
    county = CountySerializer()

    class Meta:
        model = Town
        fields = ['name', 'county']