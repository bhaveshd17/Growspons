# Generated by Django 3.2.7 on 2021-10-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_sponsor_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='profileImg',
            field=models.ImageField(upload_to='profileImg/influencer/'),
        ),
        migrations.AlterField(
            model_name='influencerpost',
            name='post_img',
            field=models.ImageField(upload_to='post/influencer/'),
        ),
    ]
