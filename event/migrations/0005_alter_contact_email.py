# Generated by Django 5.1.6 on 2025-02-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_contact_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
