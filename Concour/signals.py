import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import concourphy, concourmath, concourchimie

def delete_file_if_exists(file_field):
    """Supprime le fichier s'il existe."""
    if file_field and os.path.isfile(file_field.path):
        os.remove(file_field.path)

@receiver(post_delete, sender=concourphy)
def delete_concourphy_files(sender, instance, **kwargs):
    delete_file_if_exists(instance.epreuve)
    delete_file_if_exists(instance.corrige)

@receiver(post_delete, sender=concourmath)
def delete_concourmath_files(sender, instance, **kwargs):
    delete_file_if_exists(instance.epreuve)
    delete_file_if_exists(instance.corrige)

@receiver(post_delete, sender=concourchimie)
def delete_concourchimie_files(sender, instance, **kwargs):
    delete_file_if_exists(instance.epreuve)
    delete_file_if_exists(instance.corrige)
