from django.contrib import admin
from .models import Hero, Item, About, Contact

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('location', 'phoneNumber', 'email')

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')