from django import forms
from szabalyozok.models import Doc, Image


class DocForm(forms.ModelForm):
    doc_nev = forms.CharField(required=True, label="Dokumentum neve")
    docfile = forms.FileField(label='Feltöltés', help_text='max. 1 M')

    class Meta(forms.ModelForm):
        model = Doc
        fields = ('doc_nev', 'docfile')


class ImageForm(forms.ModelForm):
    image_nev = forms.CharField(required=True, label="Kép neve")
    image = forms.FileField(label='Feltöltés', help_text='max. 2 M')

    class Meta(forms.ModelForm):
        model = Image
        fields = ('image_nev', 'image')
