# Generated by Django 4.2 on 2023-04-19 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_agenda', '0003_alter_coordonnee_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to=settings.AUTH_USER_MODEL),
        ),
    ]
