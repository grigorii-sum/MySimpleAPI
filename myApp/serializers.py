from rest_framework import serializers

from myApp.models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        # fields = ('name', 'top_speed')
        fields = '__all__'
