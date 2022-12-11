from django.db import models

# Create your models here.
from django.db import models
from common.models import User
from aptcomplex.models import Houseinfo
# Create your models here.

class Maintenence(models.Model):
    id = models.IntegerField(max_length=4, blank=True, null = True)
    House = models.ForeignKey(Houseinfo, on_delete=models.CASCADE, default= '')
    main_date = models.IntegerField(primary_key=True)
    #main_date = models.DateField(primary_key=True)
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
    sum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'maintenence'