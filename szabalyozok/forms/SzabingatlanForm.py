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
    gps_lat = forms.CharField(required=False, label='GPS szélesség')
    gps_long = forms.CharField(required=False, label='GPS hosszúság')
    terulet_allomas = forms.DecimalField(required=False, label="Állomás területe (m2)")
    fuves_terulet = forms.DecimalField(required=False, label="Füves terület (m2)")
    burkolt_terulet = forms.DecimalField(required=False, label="Burkolt terület (m2)")
    aktiv = forms.BooleanField(required=False, initial=True, label="Aktív")
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)
    szabalyozo = forms.ModelMultipleChoiceField(queryset=Szabalyozok.objects.all(), required=False, label="Szabályozó", widget=forms.CheckboxSelectMultiple)

    class Meta(forms.ModelForm):
        model = SzabalyozokIngatlan
        fields = ('telepules', 'foldhivatali_hrsz', 'sajat_hrsz', 'fekves', 'muvelesi_ag', 'terulet_ingatlan', 'tulajdonos', 'tulajdonhanyad',
                  'tulajdonosok_szama', 'gps_lat', 'gps_long', 'terulet_allomas', 'fuves_terulet', 'burkolt_terulet', 'szabalyozo',
                  'megjegyzes', 'aktiv')