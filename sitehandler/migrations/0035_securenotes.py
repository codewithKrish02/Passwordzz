# Generated by Django 3.0.8 on 2021-08-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0034_remove_password_extensionuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='securenotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField()),
                ('name', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]