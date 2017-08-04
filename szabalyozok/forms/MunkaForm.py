from django import forms
from szabalyozok.models.SzabalyozoMunkaModel import Szabalyozomunkak, SzabalyozoMunkatipus
from szabalyozok.models.SzabalyozoMunkaModel import Muszermunkak, MuszerMunkatipus


class SzabalyozoMunkaForm(forms.ModelForm):
    szabalyozomunkatipus = forms.ModelChoiceField(queryset=SzabalyozoMunkatipus.objects.all(),
                                                  empty_label="Kérem válasszon", required=True,
                                                  label="Elvégzett munka")
    szabmunka_datum = forms.DateField(required=True, label="Munkavégzés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)
    ellenorzes = forms.BooleanField(required=False, label="Ellenőrzött")
    sap_rendelesszam = forms.CharField(required=False, label="SAP megrendelésszám")

    class Meta(forms.ModelForm):
        model = Szabalyozomunkak
        fields = ('szabalyozomunkatipus', 'szabmunka_datum', 'megjegyzes', 'ellenorzes', 'sap_rendelesszam')


class MuszerMunkaForm(forms.ModelForm):
    muszermunkatipus = forms.ModelChoiceField(queryset=MuszerMunkatipus.objects.all(), empty_label="Kérem válasszon",
                                              required=True, label="Elvégzett munka")
    muszmunka_datum = forms.DateField(required=True, label="Munkavégzés dátuma", widget=forms.TextInput(attrs={'class':'datum'}))
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)

    class Meta(forms.ModelForm):
        model = Muszermunkak
        fields = ('muszermunkatipus', 'muszmunka_datum', 'megjegyzes')
