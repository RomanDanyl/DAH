# Generated by Django 5.1.3 on 2024-11-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_location_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num_of_dreams',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
