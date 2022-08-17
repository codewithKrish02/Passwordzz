# Generated by Django 3.0.8 on 2021-08-18 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitehandler', '0021_delete_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.TextField()),
                ('website', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitehandler.extensionuser')),
            ],
        ),
    ]