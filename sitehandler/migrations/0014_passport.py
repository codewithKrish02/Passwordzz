# Generated by Django 3.0.8 on 2021-08-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0013_driverlicenseinids'),
    ]

    operations = [
        migrations.CreateModel(
            name='passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField()),
                ('name', models.TextField()),
                ('idnumber', models.TextField()),
                ('issuedate', models.TextField()),
                ('expirydate', models.TextField()),
                ('country', models.TextField()),
                ('placeofissue', models.TextField()),
            ],
        ),
    ]