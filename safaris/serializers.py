from rest_framework import serializers
from .models import Booking, SafariPackage

class SafariPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafariPackage
        fields = ['id', 'name', 'description', 'days', 'price', 'image']


class BookingSerializer(serializers.ModelSerializer):
    safari_name = serializers.CharField(source='safari.name', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'safari', 'safari_name', 'name', 'phone', 'created_at']
