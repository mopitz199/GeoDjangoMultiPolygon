from django.contrib.gis.db import models
from django.contrib.gis import geos

class Comuna(models.Model):
    nom_reg = models.CharField(max_length=50)
    nom_prov = models.CharField(max_length=20)
    nom_com = models.CharField(max_length=30)
    shape_leng = models.FloatField()
    dis_elec = models.IntegerField()
    cir_sena = models.IntegerField()
    cod_comuna = models.IntegerField()
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return "{} - {} - {}".format(self.nom_prov, self.nom_reg, self.nom_com)

    def __unicode__(self):
        return "{}".format(self.nom_prov)


class Punto(models.Model):
    point = models.PointField()

    def __str__(self):
        return "{}".format(self.point)