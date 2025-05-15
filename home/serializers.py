from rest_framework import serializers
from .models import Hero, Item
from .models import About, Contact

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'