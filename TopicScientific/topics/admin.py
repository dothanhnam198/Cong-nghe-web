from django.contrib import admin
from .models import topic, research_direction, rate, type
# Register your models here.


class research_direction_Admin(admin.ModelAdmin):
    list_display = ['research_direction']


admin.site.register(research_direction, research_direction_Admin)


class type_Admin(admin.ModelAdmin):
    list_display = ['type']


admin.site.register(type, type_Admin)


class rate_Admin(admin.ModelAdmin):
    list_display = ['rate']


admin.site.register(rate, rate_Admin)


class topic_Admin(admin.ModelAdmin):
    list_display = ['topic_name', 'author', 'research_direction', 'type', 'rate', 'review_date', 'date_upload']
    search_fields = ['research_direction__research_direction', 'type__type', 'rate__rate', 'topic_name', 'review_date', 'date_upload', 'User__author']


admin.site.register(topic, topic_Admin)