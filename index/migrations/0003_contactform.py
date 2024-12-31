# Generated by Django 5.0.6 on 2024-12-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_contactlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=400)),
            ],
        ),
    ]
