# Generated by Django 5.0.4 on 2024-05-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_member_address_member_favoritecandy_member_postid'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
