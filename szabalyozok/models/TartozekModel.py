from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from szabalyozok.models import SzabalyozoModel


class Tartozekfajta(models.Model):
    tartozekfajta = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Tartozékfajták"

    def __str__(self):
        return self.tartozekfajta


class Tartozektipus(models.Model):
    tartozekfajta = models.ForeignKey(Tartozekfajta, related_name='tart_fajta', blank=False, null=False)
    tartozekgyarto = models.ForeignKey(SzabalyozoModel.Tartozekgyartok, blank=False, null=True)
    tartozektipus = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Tartozéktípusok"
        unique_together = ('tartozekfajta', 'tartozekgyarto', 'tartozektipus')

    def __str__(self):
        return self.tartozektipus
        # return '%s - %s' % (self.tartozektipus, self.tartozekfajta)

class SzabVezerlesMod(models.Model):
    szabvezerles = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Szab. vezérlés módja"

    def __str__(self):
        return self.szabvezerles


class Tartozekok(models.Model):
    ELHELYEZKEDES_CHOICES = (
        ('', 'Kérem válasszon'),
        ('p1_ag', 'P1 ág'),
        ('p2_ag', 'P2 ág'),
        ('kozos', 'Közös'),
    )
    tartozektipus = models.ForeignKey(Tartozektipus, blank=False, null=False)
    elhelyezkedes = models.CharField(max_length=20, choices=ELHELYEZKEDES_CHOICES, )
    beuzemeles_ev = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2100)], blank=True,
                                        null=True)
    beszereles_datum = models.DateField(blank=False, null=False)
    megjegyzes = models.CharField(max_length=100, blank=True, null=True)
    szabalyozo = models.ForeignKey(SzabalyozoModel.Szabalyozok, blank=True, null=True)
    gyariszam = models.CharField(max_length=50, blank=True, null=True)
    szab_vezerles_mod = models.ForeignKey(SzabVezerlesMod, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tartozékok"

    def __str__(self):
        return str(self.tartozektipus)


class Tartozekkiszerel(models.Model):
    tartozek = models.ForeignKey(Tartozekok, related_name='tartki', blank=False, null=False)
    szabalyozo = models.ForeignKey(SzabalyozoModel.Szabalyozok, related_name='tartki_szab', blank=False, null=False)
    beszereles_datum = models.DateField(blank=True, null=True)
    kiszereles_datum = models.DateField(blank=True, null=True)
    megjegyzes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tartozék kiszerelés"

    def __str__(self):
        return str(self.tartozek)
