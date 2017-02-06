from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from szabalyozok.models import Atadok, Telepulesek, Tartozekgyartok, Szabalyozok, SzabKarb, EllenorzesiCiklus


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Név'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Jelszó'}))


class SzabalyozoForm(forms.ModelForm):
    #azonosito = forms.CharField(required=True, label="Azonosító")
    #grass_az = forms.CharField(required=False, label="Grass azonosító")
    atado = forms.ModelChoiceField(queryset=Atadok.objects.all(), empty_label="Kérem válasszon", required=True, label="Átadó")
    telepules = forms.ModelChoiceField(queryset=Telepulesek.objects.all(), empty_label="Kérem válasszon", required=True, label="Település")
    szabgyarto = forms.ModelChoiceField(queryset=Tartozekgyartok.objects.all(), empty_label="Kérem válasszon",
                                        required=True, label="Szabályozó gyártó besorolás")
    szabkarb = forms.ModelChoiceField(queryset=SzabKarb.objects.all(), empty_label="Kérem válasszon",
                                        required=False, label="Szabályozó karbantartó")
    hrsz = forms.CharField(required=False, label="HRSZ")
    gps_lat = forms.CharField(required=False, label='GPS szélesség')
    gps_long = forms.CharField(required=False, label='GPS hosszúság')
    #allomas_nev = forms.CharField(required=True, label='Állomás neve')
    aktiv = forms.BooleanField(required=False, label="Aktív")
    kivitel = forms.ChoiceField(
        required=True,
        label="Kivitel",
        widget=forms.Select,
        choices=Szabalyozok.KIVITEL_CHOICES,
    )
    elhelyezes = forms.ChoiceField(
        required=True,
        label="Elhelyezés",
        widget=forms.Select,
        choices=Szabalyozok.ELHELYEZES_CHOICES,
    )
    tulajdonjog = forms.ChoiceField(
        required=True,
        label="Tulajdonjog",
        widget=forms.Select,
        choices=Szabalyozok.TULAJDON_CHOICES,
    )
    funkcio = forms.ChoiceField(
        required=True,
        label="Funkció",
        widget=forms.Select,
        choices=Szabalyozok.FUNKCIO_CHOICES,
    )
    tulajdonos = forms.CharField(required=False, label="Tulajdonos")
    #eszkozszam = forms.CharField(required=True, label="Eszközszám")
    #beruhazasi_szam = forms.CharField(required=True, label="Beruházási szám")
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)
    nev_prim_nyom = forms.DecimalField(required=True, label="Névl. prim. nyomás")
    nev_sek_nyom = forms.DecimalField(required=True, label="Névl. szek. nyomás")
    #uz_prim_nyom = forms.DecimalField(required=True, label="Üzemi prim. nyomás")
    #uz_sek_nyom = forms.DecimalField(required=True, label="Üzemi szek. nyomás")
    nev_kapacitas = forms.IntegerField(required=True, label="Névleges kapacitás")
    nyom_din_rendszer = forms.BooleanField(required=False, label="Nyomásdinamizálási rendszer")
    futott = forms.BooleanField(required=False, label="Fűtött")
    felugyeleti_rendszer = forms.BooleanField(required=False, label="felügyeleti rendszer")
    rb_zona = forms.ChoiceField(
        required=False,
        label="Rb zóna",
        widget=forms.Select,
        choices=Szabalyozok.RBZONA_CHOICES,
    )
    #sap_pm_az = forms.CharField(required=False, label="SAP PM azonosító")
    telepites_ev = forms.IntegerField(required=False, label='Telepítés éve', min_value=1950, max_value=2100)
    villamvedelem = forms.ChoiceField(
        required=False,
        label="Villámvédelem",
        widget=forms.Select,
        choices=Szabalyozok.VILLAMVEDELEM_CHOICES,
    )
    villamvedelem_ev = forms.IntegerField(required=False, label='Villámvéd. felülvizsg. éve', min_value=1950,
                                          max_value=2100)
    villamvedelem_kov_ev = forms.IntegerField(required=False, label='Köv. villámvéd. felülvizsg. éve', min_value=1950,
                                              max_value=2100)
    karbantartas_2ev = forms.IntegerField(required=False, label='2 éves karb. köv. időpontja', min_value=1950,
                                          max_value=2100)
    karbantartas_10ev = forms.IntegerField(required=False, label='10 éves karb. köv. időpontja', min_value=1950,
                                           max_value=2100)
    osszedolg_szab = forms.CharField(required=False, label="Összedolgozó szabályozók", widget=forms.Textarea)
    ellatotttelepules = forms.ModelMultipleChoiceField(queryset=Telepulesek.objects.all(), required=True, label="Ellátott települések")
    ossz_terulet = forms.DecimalField(required=False, label="Össz. terület")
    fuves_terulet = forms.DecimalField(required=False, label="Füves terület")
    burkolt_terulet = forms.DecimalField(required=False, label="Burkolt terület")
    ellenorzesiciklus = forms.ModelChoiceField(queryset=EllenorzesiCiklus.objects.all(), empty_label="Kérem válasszon",
                                        required=False, label="Ellenőrzési ciklus")

    class Meta(forms.ModelForm):
        model = Szabalyozok
        fields = ('atado', 'telepules', 'szabgyarto', 'hrsz', 'gps_lat', 'gps_long', 'aktiv', 'kivitel',
                  'elhelyezes', 'tulajdonjog', 'funkcio', 'tulajdonos', 'megjegyzes', 'nev_prim_nyom', 'nev_sek_nyom',
                  'nev_kapacitas', 'nyom_din_rendszer', 'futott', 'felugyeleti_rendszer',
                  'rb_zona', 'telepites_ev', 'villamvedelem', 'villamvedelem_ev', 'villamvedelem_kov_ev', 'karbantartas_2ev',
                  'karbantartas_10ev', 'osszedolg_szab', 'ellatotttelepules', 'szabkarb', 'ossz_terulet', 'fuves_terulet',
                  'burkolt_terulet', 'ellenorzesiciklus')


class SearchForm(forms.Form):
    search = forms.CharField(label='', max_length=100)