from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Item(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    location = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=20)
    phoneNumberTwo = models.CharField(max_length=20, blank=True, null=True)
    instagramLink = models.URLField(max_length=255, blank=True, null=True)
    tikTokLink = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)



    def __str__(self):
        return self.location


class Hero(models.Model):
    image = models.ImageField(upload_to='hero/')
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.title