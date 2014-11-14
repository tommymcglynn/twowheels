from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from web.models import Bike, BikeStyle, BikeModel, BikePart


PAGINATE_BY_PARAM = 'page_size'


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
    paginate_by_param = PAGINATE_BY_PARAM
    max_paginate_by = 1000


class BikeStyleViewSet(viewsets.ModelViewSet):
    queryset = BikeStyle.objects.all()
    serializer_class = BikeStyleSerializer
    paginate_by = 100
    paginate_by_param = PAGINATE_BY_PARAM
    max_paginate_by = 10000


class BikeModelViewSet(viewsets.ModelViewSet):
    queryset = BikeModel.objects.all()
    serializer_class = BikeModelSerializer
    paginate_by = 100
    paginate_by_param = PAGINATE_BY_PARAM
    max_paginate_by = 10000


class BikePartViewSet(viewsets.ModelViewSet):
    queryset = BikePart.objects.all()
    serializer_class = BikePartSerializer
    paginate_by = 100
    paginate_by_param = PAGINATE_BY_PARAM
    max_paginate_by = 10000
