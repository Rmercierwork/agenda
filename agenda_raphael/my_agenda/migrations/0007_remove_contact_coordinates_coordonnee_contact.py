# Generated by Django 4.2 on 2023-04-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_agenda', '0006_remove_coordonnee_contact_remove_contact_coordinates_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='coordonnee',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='my_agenda.contact'),
        ),
    ]
