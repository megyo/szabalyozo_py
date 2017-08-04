from django import forms
from szabalyozok.models import Doc, Image, Dockategoria


class DocForm(forms.ModelForm):
    doc_nev = forms.CharField(required=True, label="Dokumentum neve")
    dockategoria = forms.ModelChoiceField(queryset=Dockategoria.objects.all(),
                                                  empty_label="Kérem válasszon", required=True,
                                                  label="Dokumentum kategória")
    docfile = forms.FileField(label='Feltöltés', help_text='max. 1 M')

    class Meta(forms.ModelForm):
        model = Doc
        fields = ('doc_nev', 'dockategoria', 'docfile')


class ImageForm(forms.ModelForm):
    image_nev = forms.CharField(required=True, label="Kép neve")
    image = forms.FileField(label='Feltöltés', help_text='max. 2 M')

    class Meta(forms.ModelForm):
        model = Image
        fields = ('image_nev', 'image')


ESZKOZ_CHOICES = (
    ('szab', 'Szabályozó állomások dokumentumai'),
    ('muszer', 'Műszerek dokumentumai'),
    ('szabmunkak', 'Szabályozó munkák dokumentumai'),
    ('muszermunkak', 'Műszer munkák dokumentumai'),
)

class DocFilterForm(forms.Form):
    doktipus = forms.ChoiceField(
        label = 'Dokumentum helye',
        required=True,
        choices=ESZKOZ_CHOICES,
    )
    dockategoria = forms.ModelChoiceField(queryset=Dockategoria.objects.all(),
                                         empty_label="--- Összes kategória ---", required=False,
                                         label="Dokumentum kategória")
    kez_datum = forms.DateField(label='Feltöltés dátumtól', required=False, widget=forms.TextInput(attrs={'class': 'datum'}))
    veg_datum = forms.DateField(label='Feltöltés dátumig', required=False, widget=forms.TextInput(attrs={'class': 'datum'}))