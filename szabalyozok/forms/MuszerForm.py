from django import forms
from szabalyozok.models import Muszerek, Muszerkiszerel, Muszertipus


class MuszerkiszerelForm(forms.Form):
    # muszer = forms.ModelChoiceField(queryset=Muszerek.objects.all(), empty_label="Kérem válasszon", required=False, label="Műszer")
    muszer = forms.CharField(required=False, label="Műszer")
    kiszereles_datum = forms.DateField(required=True, label="Kiszerelés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    selejt = forms.BooleanField(required=False, label="Selejt")
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)

    class Meta(forms.ModelForm):
        model = Muszerkiszerel
        fields = ('muszer', 'kiszereles_datum', 'selejt', 'megjegyzes')


class MuszerbeszerelForm(forms.ModelForm):
    elhelyezkedes = forms.ChoiceField(
        required=True,
        label="Elhelyezkedés",
        widget=forms.Select,
        choices=Muszerek.ELHELYEZKEDES_CHOICES,
    )
    kalib_datum = forms.DateField(required=True, label="Kalibrálás dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    kov_kalib_datum = forms.DateField(required=True, label="Következő kalib. dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    beszereles_datum = forms.DateField(required=True, label="Beszerelés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)
    #selejt = forms.BooleanField(required=False, label="Selejt")
    jegyzokonyv_szam = forms.CharField(required=False, label="Jegyzőkönyv száma")


    class Meta(forms.ModelForm):
        model = Muszerek
        fields = ('elhelyezkedes', 'kalib_datum', 'kov_kalib_datum', 'beszereles_datum', 'jegyzokonyv_szam', 'megjegyzes')


class ManometernewForm(forms.ModelForm):
    # muszergyarto = forms.ModelChoiceField(queryset=Muszergyarto.objects.all(), empty_label="Kérem válasszon", required=True,
    #                                label="Műszergyártó")
    muszertipus = forms.ModelChoiceField(queryset=Muszertipus.objects.filter(muszerfajta_id=1), empty_label="Kérem válasszon", required=True,
                                   label="Műszer típus")
    gyariszam = forms.CharField(required=True, label="Gyáriszám")
    gyartas_ev = forms.IntegerField(required=False, label='Gyártás éve', min_value=1950, max_value=2100)
    elhelyezkedes = forms.ChoiceField(
        required=False,
        label="Elhelyezkedés",
        widget=forms.Select,
        choices=Muszerek.ELHELYEZKEDES_CHOICES,
    )
    metrologia = forms.ChoiceField(
        required=True,
        label="Metrológiai jellemző",
        widget=forms.Select,
        choices=Muszerek.METROLOGIA_CHOICES,
    )
    kalib_datum = forms.DateField(required=True, label="Kalibrálás dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    kov_kalib_datum = forms.DateField(required=True, label="Következő kalib. dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    kalib_ciklusido = forms.IntegerField(required=True, label='Kalibrálási ciklusidő')
    mereshatar1 = forms.CharField(required=False, label="Méréshatár 1")
    mereshatar2 = forms.CharField(required=False, label="Méréshatár 2")
    osztalypontossag = forms.CharField(required=False, label="Osztálypontosság")
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)


    class Meta(forms.ModelForm):
        model = Muszerek
        fields = ('muszertipus', 'gyariszam', 'gyartas_ev', 'elhelyezkedes', 'metrologia', 'kalib_datum', 'kov_kalib_datum',
                  'kalib_ciklusido', 'mereshatar1', 'mereshatar2', 'osztalypontossag', 'megjegyzes')


class MuszerSearchForm(forms.Form):
    search = forms.CharField(label='', max_length=100)