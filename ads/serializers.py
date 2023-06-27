from rest_framework import serializers
from .models import Ads
from .permissions import IsPublisherOrReadOnly

class AdsSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')
    class Meta:
        model = Ads
        fields = '__all__'
        read_only_fields = ('is_public','id','created_at')
        extra_kwargs = {
            'image':{'required': False},
                        }
 