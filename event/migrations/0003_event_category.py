# Generated by Django 5.1.6 on 2025-02-06 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_contact_category_slug_event_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='event.category'),
        ),
    ]
