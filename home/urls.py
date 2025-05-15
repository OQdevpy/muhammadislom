from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet, ItemViewSet, AboutViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'about', AboutViewSet, basename='about')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'hero', HeroViewSet, basename='hero')

urlpatterns = [
    path('', include(router.urls)),
]
