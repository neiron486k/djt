from rest_framework import serializers
from .models import Pages


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        # fields = ['id', 'title']
        fields = '__all__'
