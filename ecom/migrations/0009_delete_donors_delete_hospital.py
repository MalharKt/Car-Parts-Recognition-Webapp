# Generated by Django 4.0.5 on 2023-11-06 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_alter_donors_blood_grp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Donors',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]
