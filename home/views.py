from rest_framework import viewsets
from .models import About, Contact, Hero, Item
from .serializers import AboutSerializer, ContactSerializer, HeroSerializer, ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.order_by('-id')[:1]
    serializer_class = AboutSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.order_by('-id')[:1]
    serializer_class = ContactSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer