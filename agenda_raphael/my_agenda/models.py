import re
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Agenda(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendas')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - Agenda de {self.owner.username}"


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.nom


class Coordonnee(models.Model):
    TYPES = (
        ('postale', 'Postale'),
        ('telephone', 'Téléphone'),
        ('email', 'Email'),
        ('web', 'Page Web')
    )

    type = models.CharField(max_length=15, choices=TYPES)
    valeur = models.TextField()
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='coordinates')

    def __str__(self):
        return f"{self.type} - {self.valeur}"

    def validate_postal(self):
        postal_pattern = re.compile(r'^.{10,}$')
        if not postal_pattern.match(self.valeur):
            raise ValidationError("L'adresse postale doit contenir au moins 10 caractères")

    def validate_telephone(self):
        phone_pattern = re.compile(r'^\d{10}$')
        if not phone_pattern.match(self.valeur):
            raise ValidationError("Le numéro de téléphone doit contenir exactement 10 chiffres")

    def validate_email(self):
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_pattern.match(self.valeur):
            raise ValidationError("Adresse e-mail invalide")

    def validate_web(self):
        web_pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')
        if not web_pattern.match(self.valeur):
            raise ValidationError("URL de page Web invalide")

    def clean(self):
        if self.type == 'postale':
            self.validate_postal()
        elif self.type == 'telephone':
            self.validate_telephone()
        elif self.type == 'email':
            self.validate_email()
        elif self.type == 'web':
            self.validate_web()


@receiver(post_save, sender=User)
def create_agenda(sender, instance, created, **kwargs):
    if created:
        Agenda.objects.create(owner=instance)
