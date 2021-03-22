from rest_framework import serializers
from core.models import Car, validate_popularity_not_negative,validate_range_one_to_five, Ratings


class CarSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    make = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    avg_rating = serializers.DecimalField(
        decimal_places=1,
        max_digits=2,
        required=False,
        validators=[validate_range_one_to_five],
        default=None
    )

    def create(self, validated_data):
        """
        Create and return a new `Car` instance, given the validated data.
        """
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Car` instance, given the validated data.
        """
        instance.car_make = validated_data.get('make', instance.make)
        instance.car_model = validated_data.get('model', instance.model)
        instance.avg_rating = validated_data.get('avg_rating', instance.avg_rating)
        instance.save()
        return instance

class PopularSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    make = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)
    rates_number = serializers.IntegerField(
        required=False,
        allow_null=True,
        validators=[validate_popularity_not_negative],
        default=0
    )

    # popular_list = serializers.SerializerMethodField()
    def create(self, validated_data):
        """
        Create and return a new `Car` instance, given the validated data.
        """
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Car` instance, given the validated data.
        """
        instance.car_make = validated_data.get('make', instance.make)
        instance.car_model = validated_data.get('model', instance.model)
        instance.rates_number = validated_data.get('rates_number', instance.rates_number)
        instance.save()
        return instance
class RatingSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    car_id = serializers.IntegerField()
    rating = serializers.DecimalField(
        decimal_places=1,
        max_digits=2,
        required=False,
        validators=[validate_range_one_to_five],
        default=None
    )

    def create(self, validated_data):
        return Ratings.objects.create(**validated_data)

    # def get_car_id(self, instance):
    #     return instance.car_id

