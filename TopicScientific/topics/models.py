from django.db import models

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver

# Create your models here.

class research_direction(models.Model):
    research_direction = models.CharField(max_length=50)

    def __str__(self):
        return self.research_direction


class rate(models.Model):
    rate = models.CharField(max_length=50)

    def __str__(self):
        return self.rate


class type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class topic(models.Model):
    topic_name = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    research_direction = models.ForeignKey(research_direction, on_delete=models.CASCADE)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    rate = models.ForeignKey(rate, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()
    date_upload = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)
    process = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.topic_name

    def snippet(self):
        return self.content[:50] + '...'


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + ".." + instance.topic_name)


pre_save.connect(pre_save_receiver, sender=topic)
