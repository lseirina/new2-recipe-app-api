# Generated by Django 3.2.21 on 2023-10-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20231008_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(default='Default Name', max_length=255),
        ),
    ]
