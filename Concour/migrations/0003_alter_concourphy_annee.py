# Generated by Django 5.0.7 on 2024-09-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Concour', '0002_concourphy_corrige_concourphy_electromagnetisme_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concourphy',
            name='annee',
            field=models.IntegerField(default=0),
        ),
    ]
