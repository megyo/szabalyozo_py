from django import forms
from szabalyozok.models import Muszerek, Muszerkiszerel


class MuszerkiszerelForm(forms.ModelForm):
    muszer = forms.ModelChoiceField(queryset=Muszerek.objects.all(), empty_label="Kérem válasszon", required=False, label="Műszer")
    kiszereles_datum = forms.DateField(required=True, label="Kiszerelés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    selejt = forms.BooleanField(required=False, label="Selejt")
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)

    class Meta(forms.ModelForm):
        model = Muszerkiszerel
        fields = ('muszer', 'kiszereles_datum', 'selejt', 'megjegyzes')


class MuszerbeszerelForm(forms.ModelForm):
    elhelyezkedes = forms.ChoiceField(
        required=False,
        label="Elhelyezkedés",
        widget=forms.Select,
        choices=Muszerek.ELHELYEZKEDES_CHOICES,
    )
    kalib_datum = forms.DateField(required=True, label="Kalibrálás dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    kov_kalib_datum = forms.DateField(required=True, label="Következő kalib. dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    beszereles_datum = forms.DateField(required=True, label="Beszerelés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)
    #selejt = forms.BooleanField(required=False, label="Selejt")

    class Meta(forms.ModelForm):
        model = Muszerek
        fields = ('elhelyezkedes', 'kalib_datum', 'kov_kalib_datum', 'beszereles_datum', 'megjegyzes')


class MuszerSearchForm(forms.Form):
    search = forms.CharField(label='', max_length=100)