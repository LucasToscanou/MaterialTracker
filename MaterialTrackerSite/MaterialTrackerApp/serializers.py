from rest_framework import serializers
from MaterialTrackerApp.models import *

class MTMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'