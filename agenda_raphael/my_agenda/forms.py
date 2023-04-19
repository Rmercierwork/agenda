from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Contact, Coordonnee, Agenda


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'agenda']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['agenda'].queryset = Agenda.objects.filter(owner=user)


class CoordonneeForm(ModelForm):
    class Meta:
        model = Coordonnee
        fields = ['type', 'valeur']

    def __init__(self, *args, **kwargs):
        contact = kwargs.pop('contact', None)
        super(CoordonneeForm, self).__init__(*args, **kwargs)
        if contact is not None:
            self.fields['type'].initial = contact.coordinates.all()


CoordonneeFormSet = inlineformset_factory(
    Contact, Coordonnee, form=CoordonneeForm, extra=1, can_delete=True
)


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['name']
