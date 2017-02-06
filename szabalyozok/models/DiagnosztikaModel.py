from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from szabalyozok.models import SzabalyozoModel


class DiagnosztikaOk(models.Model):
    diagnosztikaok = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Diagnosztika oka"

    def __str__(self):
        return self.diagnosztikaok


class Diagnosztika(models.Model):
    p1_nyomas = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=True)
    p2_nyomas = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=True)
    p1_also_nyomas = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    p1_felso_nyomas = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    p2_also_nyomas = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    p2_felso_nyomas = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    biztlef_nyomas = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=True)
    diag_datum = models.DateField(blank=False, null=False)
    megjegyzes = models.CharField(max_length=100, blank=True, null=True)
    szabalyozo = models.ForeignKey(SzabalyozoModel.Szabalyozok, blank=True, null=True)
    diagnosztikaok = models.ForeignKey(DiagnosztikaOk, blank=False, null=False)


    class Meta:
        verbose_name_plural = "Diagnosztika"

    def __str__(self):
        return str(self.diagnosztikaok)