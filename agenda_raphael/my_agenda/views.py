from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Contact, Agenda
from .forms import ContactForm, AgendaForm


# List of all agendas
def agenda_list(request):
    agendas = Agenda.objects.filter(owner=request.user)
    return render(request, 'my_agenda/agenda_list.html', {'agendas': agendas})


# List of all contacts
def contact_list(request):
    agenda_id = request.GET.get('agenda_id')
    if agenda_id:
        agenda = get_object_or_404(Agenda, id=agenda_id, owner=request.user)
        contacts = agenda.contacts.all()
    else:
        contacts = Contact.objects.filter(agenda__owner=request.user)
    return render(request, 'my_agenda/contact_list.html', {'contacts': contacts})


# Add a new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            agenda, created = Agenda.objects.get_or_create(owner=request.user)
            form.save(agenda)

            messages.success(request, 'Contact ajouté avec succès')
            return redirect('my_agenda:contact_list')
    else:
        form = ContactForm()
    return render(request, 'my_agenda/add_contact.html', {'form': form})


def update_contact(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact mis à jour avec succès')
            return redirect('my_agenda:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'my_agenda/update_contact.html', {'form': form})


# Remove a contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact supprimé avec succès')
        return redirect(reverse('my_agenda:contact_list'))
    return render(request, 'my_agenda/delete_contact.html', {'contact': contact})


# Create a new agenda
def add_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            agenda = form.save(commit=False)
            agenda.owner = request.user
            agenda.save()
            return redirect('my_agenda:agenda_list')
    else:
        form = AgendaForm()
    return render(request, 'my_agenda/add_agenda.html', {'form': form})


# Delete an agenda
def delete_agenda(request, pk):
    agenda = get_object_or_404(Agenda, id=pk, owner=request.user)
    if request.method == 'POST':
        agenda.delete()
        messages.success(request, 'Agenda supprimé avec succès')
        return redirect('my_agenda:agenda_list')
    return render(request, 'my_agenda/delete_agenda.html', {'agenda': agenda})