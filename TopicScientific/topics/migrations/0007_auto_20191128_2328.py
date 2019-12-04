# Generated by Django 2.2.6 on 2019-11-28 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_auto_20191128_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='rate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.rate'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]