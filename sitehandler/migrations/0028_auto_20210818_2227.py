# Generated by Django 3.0.8 on 2021-08-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0027_auto_20210818_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='uuid',
            field=models.TextField(),
        ),
    ]
