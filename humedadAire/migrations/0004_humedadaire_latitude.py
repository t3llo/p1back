# Generated by Django 3.0.5 on 2020-05-13 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humedadAire', '0003_humedadaire_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='humedadaire',
            name='latitude',
            field=models.CharField(default=1, max_length=20, verbose_name='Latitud'),
            preserve_default=False,
        ),
    ]
