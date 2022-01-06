from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from slugify import slugify



class Author(models.Model):
    name = models.CharField(max_length=265,unique=True)
    bio = models.TextField(blank=True,null=True)
    slug = AutoSlugField(populate_from=['name'])

    def get_absolute_url(self):
        return reverse('quotes:quote_add')

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.ForeignKey(Author, related_name="quotes", on_delete=models.CASCADE,blank=True,null=True)
    text = models.TextField(unique=True)

    def get_absolute_url(self):
        return reverse('quotes:random')

    def __str__(self):
        return self.text
