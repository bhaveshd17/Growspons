# Generated by Django 3.2.7 on 2021-10-11 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_merge_0004_auto_20211004_1138_0005_auto_20211003_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='profile_img',
            field=models.ImageField(upload_to='profileImg/sponsor/'),
        ),
    ]
