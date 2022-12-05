# Generated by Django 4.1.3 on 2022-12-05 15:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='car_num',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='', max_length=24, unique=True, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_num',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, null=True, region=None, unique=True),
        ),
    ]
