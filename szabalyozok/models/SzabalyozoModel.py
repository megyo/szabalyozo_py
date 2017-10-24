from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class Atadok(models.Model):
    atado = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Átadók"

    def __str__(self):
        return self.atado


class Megyek(models.Model):
    megye = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Megyék"

    def __str__(self):
        return self.megye


class Uzemek(models.Model):
    uzem = models.CharField(max_length=100, blank=False, null=False, unique=True)
    terulet = models.CharField(max_length=50, blank=False, null=False)
    jog = models.CharField(max_length=50, blank=False, null=True)

    class Meta:
        verbose_name_plural = "Üzemek"

    def __str__(self):
        return self.uzem


class Telepulesek(models.Model):
    telepules = models.CharField(max_length=100, blank=False, null=False, unique=True)
    telepules_kod = models.CharField(max_length=4, blank=False, null=False)
    uzem = models.ForeignKey(Uzemek)
    megye = models.ForeignKey(Megyek)

    class Meta:
        verbose_name_plural = "Települések"

    def __str__(self):
        return self.telepules

class Tartozekgyartok(models.Model):
    tartozekgyarto = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Tartozékgyártók"

    def __str__(self):
        return self.tartozekgyarto


class SzabKarb(models.Model):
    szabkarb = models.CharField(max_length=100, blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = "Szab. karbantartó"

    def __str__(self):
        return self.szabkarb


class EllenorzesiCiklus(models.Model):
    ellenorzesiciklus = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Ellenőrzési ciklus"

    def __str__(self):
        return self.ellenorzesiciklus


class Szabalyozok(models.Model):
    KIVITEL_CHOICES = (
        ('', 'Kérem válasszon'),
        ('1_ag', '1 ágas'),
        ('2_ag', '2 ágas'),
    )

    ELHELYEZES_CHOICES = (
        ('', 'Kérem válasszon'),
        ('akna', 'Akna'),
        ('epulet', 'Épület'),
        ('szekreny', 'Szekrény'),
    )

    TULAJDON_CHOICES = (
        ('', 'Kérem válasszon'),
        ('zrt', 'Tigáz Zrt'),
        ('dso', 'Tigáz DSO'),
        ('idegen', 'Idegen'),
    )

    RBZONA_CHOICES = (
        ('', 'Kérem válasszon'),
        ('zona_1', 'Zóna 1'),
        ('zona_2', 'Zóna 2'),
    )

    VILLAMVEDELEM_CHOICES = (
        ('', 'Kérem válasszon'),
        ('norma-uj', 'Norma szerinti'),
        ('nem_norma-regi', 'Nem norma szerinti'),
    )

    FUNKCIO_CHOICES = (
        ('', 'Kérem válasszon'),
        ('fogado', 'Fogadó'),
        ('korzeti', 'Körzeti'),
        ('ipari', 'Ipari'),
        ('egyedi', 'Egyedi'),
    )
    allomas_nev = models.CharField(max_length=255, blank=False, null=False)
    azonosito = models.CharField(max_length=10, blank=False, null=False)
    grass_az = models.CharField(max_length=21, blank=True, null=True)
    eszkozszam = models.CharField(max_length=30, blank=False, null=False)
    beruhazasi_szam = models.CharField(max_length=30, blank=False, null=False)
    sap_pm_az = models.CharField(max_length=50, blank=True, null=True)
    telepules = models.ForeignKey(Telepulesek, related_name='szabalyozo_hely')
    hrsz = models.CharField(max_length=50, blank=True, null=True)
    gps_lat = models.CharField(max_length=20, blank=True, null=True)
    gps_long = models.CharField(max_length=20, blank=True, null=True)
    atado = models.ForeignKey(Atadok)

    szabgyarto = models.ForeignKey(Tartozekgyartok, related_name='szab_gyarto', blank=True, null=True)
    szabkarb = models.ForeignKey(SzabKarb, related_name='szab_karb', blank=True, null=True)
    kivitel = models.CharField(max_length=20, choices=KIVITEL_CHOICES, blank=False, null=True)
    elhelyezes = models.CharField(max_length=20, choices=ELHELYEZES_CHOICES, blank=False, null=True)
    funkcio = models.CharField(max_length=20, blank=False, null=True, choices=FUNKCIO_CHOICES,)
    tulajdonjog = models.CharField(max_length=20, choices=TULAJDON_CHOICES,)
    tulajdonos = models.CharField(max_length=255, blank=True, null=True)
    megjegyzes = models.CharField(max_length=255, blank=True, null=True)
    nev_prim_nyom = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=False)
    nev_sek_nyom = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=False)

    uz_prim_nyom = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    uz_sek_nyom = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    nev_kapacitas = models.PositiveIntegerField(blank=True, null=True)
    nyom_din_rendszer = models.BooleanField()
    futott = models.BooleanField()
    felugyeleti_rendszer = models.BooleanField(blank=True, null=False)
    rb_zona = models.CharField(max_length=20, choices=RBZONA_CHOICES, blank=True, null=True)
    telepites_ev = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2100)], blank=True,
                                       null=True)
    villamvedelem = models.CharField(max_length=30, choices=VILLAMVEDELEM_CHOICES, blank=True, null=True)
    villamvedelem_ev = models.DateField(blank=True, null=True)
    villamvedelem_kov_ev = models.DateField(blank=True, null=True)  # models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2100)], blank=True, null=True)
    villamvedelem_szint = models.CharField(max_length=20, blank=True, null=True)

    karbantartas_2ev = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2100)], blank=True,
                                           null=True)
    karbantartas_10ev = models.IntegerField(validators=[MinValueValidator(1950), MaxValueValidator(2100)], blank=True,
                                            null=True)
    osszedolg_szab = models.CharField(max_length=255, blank=True, null=True)
    ellatotttelepules = models.ManyToManyField(Telepulesek, related_name='elltelep', related_query_name="elltelepquery")
    ossz_terulet = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    fuves_terulet = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    burkolt_terulet = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    ellenorzesiciklus = models.ForeignKey(EllenorzesiCiklus, related_name='ellen_ciklus', blank=True, null=True)
    aktiv = models.BooleanField()

    class Meta:
        verbose_name_plural = "Szabályozók"
        ordering = ['allomas_nev']

    def __str__(self):
        return self.allomas_nev