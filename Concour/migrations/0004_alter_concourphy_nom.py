# Generated by Django 5.0.7 on 2024-09-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Concour', '0003_alter_concourphy_annee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concourphy',
            name='nom',
            field=models.CharField(choices=[('CNC', 'CNC'), ('E3A', 'E3A'), ('X - ENS', 'X - ENS'), ('Mines ponts', 'Mines ponts'), ('Centrale', 'Centrale'), ('CCINP', 'CCINP')], default='CNC', max_length=15),
        ),
    ]
