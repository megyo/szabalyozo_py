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
    villamvedelem_szint = models.CharField(max_length=255)

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
    szabalyozo_id = models.CharField(max_length=20)

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
    tartozek_id = models.CharField(max_length=10)

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
    szabalyozo_id = models.CharField(max_length=20)
    ellenorzes = models.BooleanField()
    sap_rendelesszam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szabalyozok_szabmunkak_riport'


class MuszerRiport(models.Model):
    m_id = models.IntegerField()
    muszertipus = models.CharField(max_length=255)
    allomas_nev = models.CharField(max_length=255)
    elhelyezkedes = models.CharField(max_length=255)
    beszereles_datum = models.CharField(max_length=255)
    gyariszam = models.CharField(max_length=255)
    gyartas_ev = models.CharField(max_length=255)
    mereshatar1 = models.CharField(max_length=255)
    mereshatar2 = models.CharField(max_length=255)
    osztalypontossag = models.CharField(max_length=255)
    metrologia = models.CharField(max_length=255)
    kalib_ciklusido = models.CharField(max_length=255)
    kalib_datum = models.CharField(max_length=255)
    kov_kalib_datum = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    megjegyzes = models.CharField(max_length=255)
    selejt = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)
    mf_id = models.IntegerField()
    muszerfajta = models.CharField(max_length=255)
    muszergyarto = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)
    szab_id = models.IntegerField()
    jegyzokonyv_szam = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szabalyozok_muszerek_riport'


class MuszermunkaRiport(models.Model):
    munka_id = models.IntegerField()
    muszer_id = models.IntegerField()
    gyariszam = models.CharField(max_length=255)
    megjegyzes = models.CharField(max_length=255)
    muszerfajta = models.CharField(max_length=255)
    muszergyarto = models.CharField(max_length=255)
    muszertipus = models.CharField(max_length=255)
    muszermunkatipus = models.CharField(max_length=255)
    muszmunka_datum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'szabalyozok_muszermunkak_riport'


class Dok_Szabalyozo_Riport(models.Model):
    doc_nev = models.CharField(max_length=255)
    docfile = models.CharField(max_length=255)
    felt_datum = models.DateField()
    doctipus = models.CharField(max_length=255)
    # id = models.IntegerField()
    allomas_nev = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)
    dockategoria_id = models.IntegerField()
    dockategoria = models.CharField(max_length=255)
    szab_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szabalyozok_szab_dok_riport'


class Dok_Muszer_Riport(models.Model):
    doc_nev = models.CharField(max_length=255)
    docfile = models.CharField(max_length=255)
    felt_datum = models.DateField()
    doctipus = models.CharField(max_length=255)
    # id = models.IntegerField()
    allomas_nev = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)
    dockategoria_id = models.IntegerField()
    dockategoria = models.CharField(max_length=255)
    gyariszam = models.CharField(max_length=255)
    muszerfajta = models.CharField(max_length=255)
    muszergyarto = models.CharField(max_length=255)
    muszertipus = models.CharField(max_length=255)
    szab_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szabalyozok_muszer_dok_riport'


class Dok_Szabalyozo_Munka_Riport(models.Model):
    doc_nev = models.CharField(max_length=255)
    docfile = models.CharField(max_length=255)
    felt_datum = models.DateField()
    doctipus = models.CharField(max_length=255)
    # id = models.IntegerField()
    allomas_nev = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)
    dockategoria_id = models.IntegerField()
    dockategoria = models.CharField(max_length=255)
    munkatipus = models.CharField(max_length=255)
    szab_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szabalyozok_szabmunka_dok_riport'


class Dok_Muszer_Munka_Riport(models.Model):
    doc_nev = models.CharField(max_length=255)
    docfile = models.CharField(max_length=255)
    felt_datum = models.DateField()
    doctipus = models.CharField(max_length=255)
    # id = models.IntegerField()
    allomas_nev = models.CharField(max_length=255)
    jog = models.CharField(max_length=255)
    terulet = models.CharField(max_length=255)
    uzem = models.CharField(max_length=255)
    telepules = models.CharField(max_length=255)
    dockategoria_id = models.IntegerField()
    dockategoria = models.CharField(max_length=255)
    gyariszam = models.CharField(max_length=255)
    muszerfajta = models.CharField(max_length=255)
    muszergyarto = models.CharField(max_length=255)
    muszertipus = models.CharField(max_length=255)
    munkatipus = models.CharField(max_length=255)
    szab_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'szabalyozok_muszermunka_dok_riport'