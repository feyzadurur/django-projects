# Generated by Django 4.1.3 on 2024-07-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_uploadmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
