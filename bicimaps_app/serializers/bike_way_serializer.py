from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_gis.fields import GeometryField
from rest_framework.serializers import ModelSerializer
from ..models.bike_ways import BikeWays

class BikeWaysCreationSerializer(GeoFeatureModelSerializer):
    bike_way = GeometryField()

    class Meta:
        model = BikeWays
        geo_field = "bike_way"
        fields = ['name', 'bike_way', 'description']