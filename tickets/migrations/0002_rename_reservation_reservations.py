# Generated by Django 4.1.7 on 2023-03-18 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservation',
            new_name='Reservations',
        ),
    ]
