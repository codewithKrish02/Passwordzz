# Generated by Django 3.1.4 on 2021-08-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0037_remove_extensionuser_randomkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionuser',
            name='randomkey',
            field=models.TextField(default=None),
        ),
    ]
