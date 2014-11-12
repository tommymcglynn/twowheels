from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from web.models import Bike, BikeStyle, BikeModel, BikePart


class BikeStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeStyle
        fields = ('id', 'name')


class BikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeModel
        fields = ('id', 'type', 'name')


class BikePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikePart
        fields = ('id', 'type', 'name')


class BikeSerializer(serializers.HyperlinkedModelSerializer):
    styles = BikeStyleSerializer(many=True)
    models = BikeModelSerializer(many=True)
    parts = BikePartSerializer(many=True)

    class Meta:
        model = Bike
        fields = ('url', 'id', 'name', 'image_url', 'styles', 'models', 'parts')


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    paginate_by = 20
    paginate_by_param = 'page_size'
    max_paginate_by = 1000
