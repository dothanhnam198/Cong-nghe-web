# Generated by Django 2.2.6 on 2019-11-25 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20191125_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='acceptance_date',
            new_name='review_date',
        ),
    ]
