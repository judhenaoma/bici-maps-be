from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from ..models.review import Review
from rest_framework_gis.fields import GeometryField
from rest_framework.fields import CharField


class ReviewSerializer(GeoFeatureModelSerializer):

    review_location = GeometryField()
    # user_id = CharField()

    class Meta:
        model = Review
        geo_field = "review_location"
        # fields = '__all__'
        fields = ['review_id','review_location', 'review']
