# Generated by Django 3.0.8 on 2021-08-18 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0009_companyinpersonalinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='websiteinpersonalinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField()),
                ('websiteurl', models.TextField()),
                ('nameofwebsite', models.TextField()),
            ],
        ),
    ]
