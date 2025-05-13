from rest_framework import viewsets
from .models import About, Contact, Item
from .serializers import AboutSerializer, ContactSerializer, ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.order_by('-id')[:1]
    serializer_class = AboutSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.order_by('-id')[:1]
    serializer_class = ContactSerializer