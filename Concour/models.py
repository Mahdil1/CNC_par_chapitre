from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.core.exceptions import ValidationError

def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Seuls les fichiers PDF sont autorisés.')


# Create your models here.

class concourphy(models.Model):
    concour = [
        ('CNC','CNC'),
        ('E3A', 'E3A'),
        ('X - ENS', 'X - ENS'),
        ('Mines ponts', 'Mines ponts'),
        ('Centrale', 'Centrale'),
        ('CCINP', 'CCINP')
    ]
    fil = [('MP', 'MP'), ('PSI', 'PSI'), ('TSI', 'TSI')]
    epr = [('physique 1', 'physique 1'), ('physique 2', 'physique 2')]
    nom = models.CharField(max_length=15, choices=concour, default='CNC')
    annee = models.IntegerField(default=0)
    filier = models.CharField(max_length=10, choices=fil, default='MP')
    numepreuve = models.CharField(max_length=10, choices=epr, default='physique 1')
    mecanique = models.BooleanField(default=False)
    electromagnetisme = models.BooleanField(default=False)
    thermodynamique = models.BooleanField(default=False)
    optique = models.BooleanField(default=False)
    quantique = models.BooleanField(default=False)
    electronique = models.BooleanField(default=False)
    details = models.CharField(max_length=200, default='Détails non fournis')
    #epreuve = models.FileField(upload_to='epreuve/%Y/%m/%d', null=True, blank=True)
    #corrige = models.FileField(upload_to='corrige/%Y/%m/%d', null=True, blank=True)

    # Stockage des fichiers PDF sur Cloudinary avec validation
    epreuve = models.FileField(
        storage=RawMediaCloudinaryStorage(),
        upload_to="epreuves/physique/%Y",
        validators=[validate_pdf],
        null=True,
        blank=True
    )

    corrige = models.FileField(
        storage=RawMediaCloudinaryStorage(),
        upload_to="corriges/physique/%Y",
        validators=[validate_pdf],
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nom} - {self.annee} - {self.numepreuve}"

class concourmath(models.Model):
    concour = [
        ('CNC','CNC'),
        ('E3A', 'E3A'),
        ('X - ENS', 'X - ENS'),
        ('Mines ponts', 'Mines ponts'),
        ('Centrale', 'Centrale'),
        ('CCINP', 'CCINP')
    ]
    fil = [('MP', 'MP'), ('PSI', 'PSI'), ('TSI', 'TSI')]
    epr = [('mathématiques 1', 'mathematiques 1'), ('mathematiques 2', 'mathematiques 2')]
    nom = models.CharField(max_length=15, choices=concour, default='CNC')
    annee = models.IntegerField(default=0)
    filier = models.CharField(max_length=10, choices=fil, default='MP')
    numepreuve = models.CharField(max_length=15, choices=epr, default='mathematiques 1')
    algebre = models.BooleanField(default=False)
    analyse = models.BooleanField(default=False)
    proba = models.BooleanField(default=False)
    geometrie = models.BooleanField(default=False)
    details = models.CharField(max_length=200, default='Détails non fournis')
    #epreuve = models.FileField(upload_to='epreuve/%Y/%m/%d', null=True, blank=True)
    #corrige = models.FileField(upload_to='corrige/%Y/%m/%d', null=True, blank=True)

    # Stockage des fichiers PDF sur Cloudinary avec validation
    epreuve = models.FileField(
        storage=RawMediaCloudinaryStorage(),
        upload_to="epreuves/math/%Y",
        validators=[validate_pdf],
        null=True,
        blank=True
    )

    corrige = models.FileField(
        storage=RawMediaCloudinaryStorage(),
        upload_to="corriges/math/%Y",
        validators=[validate_pdf],
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nom} - {self.annee} - {self.numepreuve}"


class concourchimie(models.Model):
    concour = [
        ('CNC','CNC'),
        ('E3A', 'E3A'),
        ('X - ENS', 'X - ENS'),
        ('Mines ponts', 'Mines ponts'),
        ('Centrale', 'Centrale'),
        ('CCINP', 'CCINP')
    ]
    fil = [('MP', 'MP'), ('PSI', 'PSI'), ('TSI', 'TSI')]
    nom = models.CharField(max_length=15, choices=concour, default='CNC')
    annee = models.IntegerField(default=0)
    filier = models.CharField(max_length=10, choices=fil, default='MP')
    generale = models.BooleanField(default=False)
    thermochimie = models.BooleanField(default=False)
    electrochimie = models.BooleanField(default=False)
    cinetique = models.BooleanField(default=False)
    diag_bin = models.BooleanField(default=False)
    solution = models.BooleanField(default=False)
    organique = models.BooleanField(default=False)
    details = models.CharField(max_length=200, default='Détails non fournis')
    #epreuve = models.FileField(upload_to='epreuve/%Y/%m/%d', null=True, blank=True)
    #corrige = models.FileField(upload_to='corrige/%Y/%m/%d', null=True, blank=True)

    # Stockage des fichiers PDF sur Cloudinary avec validation
    epreuve = models.FileField(
        storage=RawMediaCloudinaryStorage(),
        upload_to="epreuves/chimie/%Y",
        validators=[validate_pdf],
        null=True,
        blank=True
    )

    corrige = models.FileField(
        storage=RawMediaCloudinaryStorage(),
        upload_to="corriges/chimie/%Y",
        validators=[validate_pdf],
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nom} - {self.annee} - {self.numepreuve}"



