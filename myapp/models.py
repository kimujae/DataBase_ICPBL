# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Maintenence(models.Model):
    main_date = models.IntegerField(primary_key=True)
    heatc = models.BigIntegerField(blank=True, null=True)
    heatp = models.BigIntegerField(blank=True, null=True)
    electc = models.BigIntegerField(blank=True, null=True)
    electp = models.BigIntegerField(blank=True, null=True)
    gasc = models.BigIntegerField(blank=True, null=True)
    gasp = models.BigIntegerField(blank=True, null=True)
    waterhotc = models.BigIntegerField(blank=True, null=True)
    waterhotp = models.BigIntegerField(blank=True, null=True)
    watercoolc = models.BigIntegerField(blank=True, null=True)
    watercoolp = models.BigIntegerField(blank=True, null=True)
    domesticwaste = models.BigIntegerField(blank=True, null=True)
    waterpruifier = models.BigIntegerField(blank=True, null=True)
    representation = models.BigIntegerField(blank=True, null=True)
    election = models.BigIntegerField(blank=True, null=True)
    buildingin = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenence'
