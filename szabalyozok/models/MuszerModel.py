from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from szabalyozok.models import SzabalyozoModel


class Muszerfajta(models.Model):
    muszerfajta = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Műszerfajták"

    def __str__(self):
        return self.muszerfajta


class Muszergyarto(models.Model):
    muszergyarto = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Műszergyártók"

    def __str__(self):
        return self.muszergyarto


class Muszertipus(models.Model):
    muszerfajta = models.ForeignKey(Muszerfajta, related_name='muszer_fajta', blank=False, null=False)
    muszergyarto = models.ForeignKey(Muszergyarto, blank=False, null=False)
    muszertipus = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Műszertípusok"

    def __str__(self):
        return self.muszertipus


class Muszerek(models.Model):
    ELHELYEZKEDES_CHOICES = (
        ('', 'Kérem válasszon'),
        ('p1_ag', 'P1 ág'),
        ('p2_ag', 'P2 ág'),
        ('kozos', 'Közös'),
    )
    METROLOGIA_CHOICES = (
        ('', 'Kérem válasszon'),
        ('H', 'Hitelesítendő'),
        ('K', 'Kalibrálandó'),
        ('FH', 'Helyszínen felülvizsgálandó'),
        ('FM', 'Műhelyben felülvizsgálandó'),
        ('T', 'Tájékoztató jellegű'),
        ('Cs', 'Cserélendő'),
    )
    muszertipus = models.ForeignKey(Muszertipus, blank=False, null=False)
    szabalyozo = models.ForeignKey(SzabalyozoModel.Szabalyozok, blank=True, null=True)
    elhelyezkedes = models.CharField(max_length=20, choices=ELHELYEZKEDES_CHOICES, blank=True, null=True)
    beszereles_datum = models.DateField(blank=True, null=True)
    gyariszam = models.CharField(max_length=50, blank=False, null=False)
    gyartas_ev = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2100)], blank=True,
                                     null=True)
    mereshatar1 = models.CharField(max_length=20, blank=True, null=True)
    mereshatar2 = models.CharField(max_length=20, blank=True, null=True)
    osztalypontossag = models.CharField(max_length=20, blank=True, null=True)
    metrologia = models.CharField(max_length=50, choices=METROLOGIA_CHOICES, )
    kalib_ciklusido = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], blank=False,
                                          null=False)
    kalib_datum = models.DateField(blank=True, null=True)
    kov_kalib_datum = models.DateField(blank=True, null=True)
    telefon = models.CharField(max_length=100, blank=True, null=True)
    megjegyzes = models.CharField(max_length=100, blank=True, null=True)
    selejt = models.BooleanField()

    class Meta:
        verbose_name_plural = "Műszerek"
        unique_together = ('muszertipus', 'gyariszam')

    def __str__(self):
        return str(self.muszertipus)


class Muszerkiszerel(models.Model):
    muszer = models.ForeignKey(Muszerek, related_name='muszerki', blank=False, null=False)
    szabalyozo = models.ForeignKey(SzabalyozoModel.Szabalyozok, related_name='muszerki_szab', blank=False, null=False)
    beszereles_datum = models.DateField(blank=True, null=True)
    kiszereles_datum = models.DateField(blank=True, null=True)
    megjegyzes = models.CharField(max_length=100, blank=True, null=True)
    selejt = models.BooleanField()

    class Meta:
        verbose_name_plural = "Műszer kiszerelés"

    def __str__(self):
        return str(self.muszer)
