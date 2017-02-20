from django.db import models


class SzabalyozokRiport(models.Model):
    allomas_nev = models.CharField(max_length=255)
    azonosito = models.CharField(max_length=10)
    grass_az = models.CharField(max_length=11)
    eszkozszam = models.CharField(max_length=30)
    beruhazasi_szam = models.CharField(max_length=30)
    sap_pm_az = models.CharField(max_length=20)
    telepules = models.CharField(max_length=255)
    hrsz = models.CharField(max_length=10)
    gps_lat = models.CharField(max_length=20)
    gps_long = models.CharField(max_length=20)
    atado = models.CharField(max_length=255)
    tartozekgyarto = models.CharField(max_length=255)
    szabkarb = models.CharField(max_length=255)
    kivitel = models.CharField(max_length=255)
    elhelyezes = models.CharField(max_length=255)
    funkcio = models.CharField(max_length=255)
    tulajdonjog = models.CharField(max_length=255)
    tulajdonos = models.CharField(max_length=255)
    megjegyzes = models.CharField(max_length=255)
    nev_prim_nyom = models.CharField(max_length=255)
    nev_sek_nyom = models.CharField(max_length=255)
    uz_prim_nyom = models.CharField(max_length=255)
    uz_sek_nyom = models.CharField(max_length=255)
    nev_kapacitas = models.CharField(max_length=255)
    nyom_din_rendszer = models.BooleanField()
    futott = models.CharField(max_length=255)
    felugyeleti_rendszer = models.BooleanField()
    rb_zona = models.CharField(max_length=255)
    telepites_ev = models.CharField(max_length=255)
    villamvedelem = models.CharField(max_length=255)
    villamvedelem_ev = models.CharField(max_length=255)
    villamvedelem_kov_ev = models.CharField(max_length=255)
    karbantartas_2ev = models.CharField(max_length=255)
    karbantartas_10ev = models.CharField(max_length=255)
    osszedolg_szab = models.CharField(max_length=255)
    ossz_terulet = models.CharField(max_length=255)
    fuves_terulet = models.CharField(max_length=255)
    burkolt_terulet = models.CharField(max_length=255)
    aktiv = models.BooleanField()
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    telepules_kod = models.CharField(max_length=255)
    osszedolg_szab = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)
    ellenorzesiciklus = models.CharField(max_length=255)
    ellatott = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szabalyozok_szabalyozok_riport'


class DiagnosztikaRiport(models.Model):
    allomas_nev = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    p1_nyomas = models.CharField(max_length=255)
    p2_nyomas = models.CharField(max_length=255)
    p1_also_nyomas = models.CharField(max_length=255)
    p1_felso_nyomas = models.CharField(max_length=255)
    p2_also_nyomas = models.CharField(max_length=255)
    p2_felso_nyomas = models.CharField(max_length=255)
    biztlef_nyomas = models.CharField(max_length=255)
    diag_datum = models.CharField(max_length=255)
    megjegyzes = models.CharField(max_length=255)
    allomas_nev = models.CharField(max_length=255)
    diagnosztikaok = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szabalyozok_diagnosztika_riport'


class TartozekRiport(models.Model):
    tartozektipus = models.CharField(max_length=255)
    elhelyezkedes = models.CharField(max_length=255)
    beuzemeles_ev = models.CharField(max_length=255)
    beszereles_datum = models.CharField(max_length=255)
    megjegyzes = models.CharField(max_length=255)
    allomas_nev = models.CharField(max_length=255)
    gyariszam = models.CharField(max_length=255)
    szabvezerles = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)
    tartozekfajta = models.CharField(max_length=255)
    tartozekgyarto = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szabalyozok_tartozekok_riport'


class SzabmunkakRiport(models.Model):
    allomas_nev = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    szabalyozomunkatipus = models.CharField(max_length=255)
    szabmunka_datum = models.CharField(max_length=255)
    megjegyzes = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szabalyozok_szabmunkak_riport'