from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from web.models import Bike, BikeStyle, BikeMake, BikeFamily, BikeModel, BikePart


PAGINATE_BY_PARAM = 'page_size'


class BikeStyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikeStyle
        fields = ('url', 'id', 'name')


class BikeMakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikeMake
        fields = ('url', 'id', 'name')


class BikeFamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikeFamily
        fields = ('url', 'id', 'name', 'make')


class BikeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikeModel
        fields = ('url', 'id', 'name', 'family')


class BikePartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikePart
        fields = ('url', 'id', 'type', 'name')


class BikeSerializer(serializers.HyperlinkedModelSerializer):
    model = BikeModelSerializer()
    styles = BikeStyleSerializer(many=True)
    parts = BikePartSerializer(many=True)

    class Meta:
        model = Bike
        fields = ('url', 'created', 'id', 'name', 'image_url', 'source_url', 'model', 'styles', 'parts')


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


class BikeMakeViewSet(viewsets.ModelViewSet):
    queryset = BikeMake.objects.all()
    serializer_class = BikeMakeSerializer
    paginate_by = 100
    paginate_by_param = PAGINATE_BY_PARAM
    max_paginate_by = 10000


class BikeFamilyViewSet(viewsets.ModelViewSet):
    queryset = BikeFamily.objects.all()
    serializer_class = BikeFamilySerializer
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
