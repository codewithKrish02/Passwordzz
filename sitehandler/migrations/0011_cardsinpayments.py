# Generated by Django 3.0.8 on 2021-08-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0010_websiteinpersonalinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardsinpayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField()),
                ('cardholdername', models.TextField()),
                ('cardnumber', models.TextField()),
                ('cvv', models.TextField()),
                ('expirymonth', models.TextField()),
                ('expiryyear', models.TextField()),
                ('nameofcard', models.TextField()),
            ],
        ),
    ]
