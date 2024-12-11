# Generated by Django 5.0.7 on 2024-09-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Concour', '0006_alter_concourphy_corrige_alter_concourphy_epreuve'),
    ]

    operations = [
        migrations.CreateModel(
            name='concourchimie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('CNC', 'CNC'), ('E3A', 'E3A'), ('X - ENS', 'X - ENS'), ('Mines ponts', 'Mines ponts'), ('Centrale', 'Centrale'), ('CCINP', 'CCINP')], default='CNC', max_length=15)),
                ('annee', models.IntegerField(default=0)),
                ('filier', models.CharField(choices=[('MP', 'MP'), ('PSI', 'PSI'), ('TSI', 'TSI')], default='MP', max_length=10)),
                ('generale', models.BooleanField(default=False)),
                ('thermochimie', models.BooleanField(default=False)),
                ('electrochimie', models.BooleanField(default=False)),
                ('cinetique', models.BooleanField(default=False)),
                ('diag_bin', models.BooleanField(default=False)),
                ('solution', models.BooleanField(default=False)),
                ('organique', models.BooleanField(default=False)),
                ('epreuve', models.FileField(blank=True, null=True, upload_to='epreuve/%Y/%m/%d')),
                ('corrige', models.FileField(blank=True, null=True, upload_to='corrige/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='concourmath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(choices=[('CNC', 'CNC'), ('E3A', 'E3A'), ('X - ENS', 'X - ENS'), ('Mines ponts', 'Mines ponts'), ('Centrale', 'Centrale'), ('CCINP', 'CCINP')], default='CNC', max_length=15)),
                ('annee', models.IntegerField(default=0)),
                ('filier', models.CharField(choices=[('MP', 'MP'), ('PSI', 'PSI'), ('TSI', 'TSI')], default='MP', max_length=10)),
                ('numepreuve', models.CharField(choices=[('mathématiques 1', 'mathematiques 1'), ('mathematiques 2', 'mathematiques 2')], default='mathematiques 1', max_length=15)),
                ('algebre', models.BooleanField(default=False)),
                ('analyse', models.BooleanField(default=False)),
                ('proba', models.BooleanField(default=False)),
                ('geometrie', models.BooleanField(default=False)),
                ('epreuve', models.FileField(blank=True, null=True, upload_to='epreuve/%Y/%m/%d')),
                ('corrige', models.FileField(blank=True, null=True, upload_to='corrige/%Y/%m/%d')),
            ],
        ),
    ]
