from django import forms
from szabalyozok.models import SzabalyozokIngatlan, Telepulesek, Szabalyozok


class SzabIngatlanForm(forms.ModelForm):
    fekves = forms.ChoiceField(
        required=True,
        label="Fekvés",
        widget=forms.Select,
        choices=SzabalyozokIngatlan.FEKVES_CHOICES,
    )
    tulajdonos = forms.ChoiceField(
        required=False,
        label="Tulajdon",
        widget=forms.Select,
        choices=SzabalyozokIngatlan.TULAJDONOS_CHOICES,
    )

    telepules = forms.ModelChoiceField(queryset=Telepulesek.objects.all(), empty_label="Kérem válasszon", required=True,
                                       label="Település")
    foldhivatali_hrsz = forms.CharField(required=True, label="Földhivatali HRSZ")
    sajat_hrsz = forms.CharField(required=False, label="Saját HRSZ")
    muvelesi_ag = forms.CharField(required=True, label="Művelési ág")
    terulet_ingatlan = forms.DecimalField(required=True, label="Ingatlan területe (m2)")
    tulajdonhanyad = forms.CharField(required=False, label="Tulajdon hányad")
    tulajdonosok_szama = forms.IntegerField(required=False, label='Tulajdonosok száma')

    aktiv = forms.BooleanField(required=False, initial=True, label="Aktív")
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)
    szabalyozo = forms.ModelMultipleChoiceField(queryset=Szabalyozok.objects.all(), required=False, label="Szabályozó", widget=forms.CheckboxSelectMultiple)

    jogosultsag_allapot = forms.ChoiceField(
        required=False,
        label="Jogosutság állapot",
        widget=forms.Select,
        choices=SzabalyozokIngatlan.JOGOSULTSAG_ALLAPOT_CHOICES,
    )

    jogosultsag_tipus_1 = forms.ChoiceField(
        required=False,
        label="Jogosutság típus 1",
        widget=forms.Select,
        choices=SzabalyozokIngatlan.JOGOSULTSAG_TIPUS,
    )
    jogosultsag_m2_1 = forms.DecimalField(required=False, label="Jogosult m2 1")
    jogosultsag_nev_1 = forms.CharField(required=False, label="Jogosult név 1")

    jogosultsag_tipus_2 = forms.ChoiceField(
        required=False,
        label="Jogosutság típus 2",
        widget=forms.Select,
        choices=SzabalyozokIngatlan.JOGOSULTSAG_TIPUS,
    )
    jogosultsag_m2_2 = forms.DecimalField(required=False, label="Jogosult m2 2")
    jogosultsag_nev_2 = forms.CharField(required=False, label="Jogosult név 2")

    jogosultsag_tipus_3 = forms.ChoiceField(
        required=False,
        label="Jogosutság típus 3",
        widget=forms.Select,
        choices=SzabalyozokIngatlan.JOGOSULTSAG_TIPUS,
    )
    jogosultsag_m2_3 = forms.DecimalField(required=False, label="Jogosult m2 3")
    jogosultsag_nev_3 = forms.CharField(required=False, label="Jogosult név 3")

    gps_lat = forms.CharField(required=False, label='GPS szélesség 1')
    gps_long = forms.CharField(required=False, label='GPS hosszúság 1')

    gps_lat_2 = forms.CharField(required=False, label='GPS szélesség 2')
    gps_long_2 = forms.CharField(required=False, label='GPS hosszúság 2')

    gps_lat_3 = forms.CharField(required=False, label='GPS szélesség 3')
    gps_long_3 = forms.CharField(required=False, label='GPS hosszúság 3')

    gps_lat_4 = forms.CharField(required=False, label='GPS szélesség 4')
    gps_long_4 = forms.CharField(required=False, label='GPS hosszúság 4')

    class Meta(forms.ModelForm):
        model = SzabalyozokIngatlan
        fields = ('telepules', 'foldhivatali_hrsz', 'sajat_hrsz', 'fekves', 'muvelesi_ag', 'terulet_ingatlan',
                  'tulajdonos', 'tulajdonhanyad', 'tulajdonosok_szama',
                  'gps_lat', 'gps_long', 'gps_lat_2', 'gps_long_2', 'gps_lat_3', 'gps_long_3', 'gps_lat_4', 'gps_long_4',
                  'szabalyozo', 'jogosultsag_allapot', 'jogosultsag_tipus_1','jogosultsag_m2_1',
                  'jogosultsag_nev_1', 'jogosultsag_tipus_2','jogosultsag_m2_2', 'jogosultsag_nev_2',
                  'jogosultsag_tipus_3','jogosultsag_m2_3', 'jogosultsag_nev_3', 'megjegyzes', 'aktiv')