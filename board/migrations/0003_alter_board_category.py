# Generated by Django 4.1.3 on 2022-11-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(max_length=6),
        ),
    ]
