from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Item(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.title
