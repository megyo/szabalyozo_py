from django import forms
from szabalyozok.models import Tartozekgyartok
from szabalyozok.models import Tartozekok, Tartozekfajta, Tartozektipus, Tartozekkiszerel, SzabVezerlesModel


class TartozekForm(forms.ModelForm):
    elhelyezkedes = forms.ChoiceField(
        required=True,
        label="Elhelyezkedés",
        widget=forms.Select,
        choices=Tartozekok.ELHELYEZKEDES_CHOICES,
    )
    tartozekfajta = forms.ModelChoiceField(queryset=Tartozekfajta.objects.all(), empty_label="Kérem válasszon", required=True, label="Tartozék fajta")
    tartozekgyarto = forms.ModelChoiceField(queryset=Tartozekgyartok.objects.all(), empty_label="Kérem válasszon", required=True, label="Tartozék gyártó")
    tartozektipus = forms.ModelChoiceField(queryset=Tartozektipus.objects.all(), empty_label="Kérem válasszon", required=True, label="Tartozék típus")
    gyariszam = forms.CharField(required=False, label="Gyáriszám")
    szabvezerles = forms.ModelChoiceField(queryset=SzabVezerlesModel.objects.all(), empty_label="Kérem válasszon", required=False, label="Szab. vezérlés módja")
    beuzemeles_ev = forms.IntegerField(required=False, label='Beüzemelés éve', min_value=1950, max_value=2100)
    beszereles_datum = forms.DateField(required=True, label="Beszerelés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)


    class Meta(forms.ModelForm):
        model = Tartozekok
        fields = ('tartozekfajta', 'tartozekgyarto', 'tartozektipus', 'gyariszam', 'szabvezerles', 'elhelyezkedes', 'beuzemeles_ev', 'beszereles_datum', 'megjegyzes')


class TartozekkiszerelForm(forms.ModelForm):
    tartozek = forms.ModelChoiceField(queryset=Tartozekok.objects.all(), empty_label="Kérem válasszon", required=False, label="Tartozék")
    kiszereles_datum = forms.DateField(required=True, label="Kiszerelés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)

    class Meta(forms.ModelForm):
        model = Tartozekkiszerel
        fields = ('tartozek', 'kiszereles_datum', 'megjegyzes')