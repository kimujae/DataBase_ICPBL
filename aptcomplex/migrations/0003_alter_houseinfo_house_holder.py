# Generated by Django 4.1.3 on 2022-12-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aptcomplex", "0002_alter_houseinfo_house_holder"),
    ]

    operations = [
        migrations.AlterField(
            model_name="houseinfo",
            name="house_holder",
            field=models.CharField(blank=True, max_length=16),
        ),
    ]