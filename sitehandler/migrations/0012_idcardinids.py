# Generated by Django 3.0.8 on 2021-08-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0011_cardsinpayments'),
    ]

    operations = [
        migrations.CreateModel(
            name='idcardinids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField()),
                ('name', models.TextField()),
                ('idnumber', models.TextField()),
                ('issuedate', models.TextField()),
                ('expirydate', models.TextField()),
                ('country', models.TextField()),
            ],
        ),
    ]
