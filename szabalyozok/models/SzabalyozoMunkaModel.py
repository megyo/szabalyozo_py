from django.db import models
from szabalyozok.models import SzabalyozoModel
from szabalyozok.models import MuszerModel


class SzabalyozoMunkatipus(models.Model):
    szabalyozomunkatipus = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Szabályozó munkatípusok"

    def __str__(self):
        return self.szabalyozomunkatipus


class MuszerMunkatipus(models.Model):
    muszermunkatipus = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Műszer munkatípusok"

    def __str__(self):
        return self.muszermunkatipus


class Szabalyozomunkak(models.Model):
    szabalyozomunkatipus = models.ForeignKey(SzabalyozoMunkatipus, related_name='szabmunka_tipus', blank=False,
                                             null=False)
    szabmunka_datum = models.DateField(blank=False, null=False)
    megjegyzes = models.CharField(max_length=100, blank=True, null=True)
    szabalyozo = models.ForeignKey(SzabalyozoModel.Szabalyozok, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Szabályozó munkák"

    def __str__(self):
        return str(self.szabalyozomunkatipus)


class Muszermunkak(models.Model):
    muszermunkatipus = models.ForeignKey(MuszerMunkatipus, related_name='muszermunka_tipus', blank=False, null=False)
    muszmunka_datum = models.DateField(blank=False, null=False)
    megjegyzes = models.CharField(max_length=100, blank=True, null=True)
    muszer = models.ForeignKey(MuszerModel.Muszerek, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Műszer munkák"

    def __str__(self):
        return str(self.muszermunkatipus)
