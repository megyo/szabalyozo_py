from django.db import models
from szabalyozok.models import Telepulesek, Szabalyozok


class SzabalyozokIngatlan(models.Model):
    FEKVES_CHOICES = (
        ('', 'Kérem válasszon'),
        ('Belterület', 'Belterület'),
        ('Külterület', 'Külterület'),
        ('Zártkert', 'Zártkert'),
    )

    TULAJDONOS_CHOICES = (
        ('', 'Kérem válasszon'),
        ('Saját', 'Saját tulajdon'),
        ('Idegen', 'Idegen tulajdon'),
        ('Rész', 'Rész tulajdon'),
    )

    telepules = models.ForeignKey(Telepulesek, related_name='ingatlan_telepules', blank=False, null=False)
    foldhivatali_hrsz = models.CharField(max_length=50, blank=False, null=False)
    sajat_hrsz = models.CharField(max_length=50, blank=True, null=True)
    fekves = models.CharField(max_length=100, choices=FEKVES_CHOICES, blank=False, null=False)
    muvelesi_ag = models.CharField(max_length=255, blank=False, null=False)
    terulet_ingatlan = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    tulajdonos = models.CharField(max_length=100, choices=TULAJDONOS_CHOICES, blank=True, null=True)
    tulajdonhanyad = models.CharField(max_length=255, blank=True, null=True)
    tulajdonosok_szama = models.IntegerField(blank=True, null=True)

    gps_lat = models.CharField(max_length=20, blank=True, null=True)
    gps_long = models.CharField(max_length=20, blank=True, null=True)
    terulet_allomas = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    fuves_terulet = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    burkolt_terulet = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    szabalyozo = models.ManyToManyField(Szabalyozok, related_name='szabalyozok_ingatlan', related_query_name="szabalyozok_ingatlan_query", blank=True, null=True)

    aktiv = models.BooleanField()
    megjegyzes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Ingatlan"
        ordering = ['telepules']
        unique_together = ('telepules', 'foldhivatali_hrsz')

    def __str__(self):
        return str(self.telepules) + " - " + str(self.foldhivatali_hrsz)