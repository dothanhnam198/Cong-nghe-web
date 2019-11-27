# Generated by Django 2.2.6 on 2019-11-24 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='research_direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_direction', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('date_upload', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.rate')),
                ('research_direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.research_direction')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.type')),
            ],
        ),
    ]
