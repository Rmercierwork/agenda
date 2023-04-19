from django import forms
from .models import Contact, Coordonnee, Agenda


class CoordonneeForm(forms.ModelForm):
    class Meta:
        model = Coordonnee
        fields = ['type', 'valeur']

    def clean(self):
        cleaned_data = super().clean()
        coordonnee = self.instance
        coordonnee.clean()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom']

    postal = forms.CharField(required=False, label='Adresse postale')
    phone = forms.CharField(required=False, label='Numéro de téléphone')
    email = forms.EmailField(required=False, label='E-mail')
    web = forms.URLField(required=False, label='Page Web')

    def __init__(self, *args, **kwargs):
        contact = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

        if contact:
            initial_values = {'postal': '', 'phone': '', 'email': '', 'web': ''}
            for coord in contact.coordonnees.all():
                initial_values[coord.type] = coord.valeur
            self.fields['postal'].initial = initial_values['postal']
            self.fields['phone'].initial = initial_values['phone']
            self.fields['email'].initial = initial_values['email']
            self.fields['web'].initial = initial_values['web']

    def save(self, agenda, commit=True):
        contact = super().save(commit=False)
        contact.agenda = agenda
        contact.save()

        coord_types = ['postal', 'phone', 'email', 'web']
        for coord_type in coord_types:
            value = self.cleaned_data[coord_type]
            if value:
                coord, created = Coordonnee.objects.get_or_create(contact=contact, type=coord_type)
                coord.valeur = value
                coord.save()
            else:
                Coordonnee.objects.filter(contact=contact, type=coord_type).delete()

        return contact


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['name']
