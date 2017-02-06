from django import forms
from szabalyozok.models import Diagnosztika, DiagnosztikaOk


class DiagnosztikaForm(forms.ModelForm):
    p1_nyomas = forms.DecimalField(required=True, label="Üzemi prim. nyomás")
    p2_nyomas = forms.DecimalField(required=True, label="Üzemi sek. nyomás")
    p1_also_nyomas = forms.DecimalField(required=False, label="P1 ág alsó")
    p1_felso_nyomas = forms.DecimalField(required=False, label="P1 ág felső")
    p2_also_nyomas = forms.DecimalField(required=False, label="P2 ág alsó")
    p2_felso_nyomas = forms.DecimalField(required=False, label="P2 ág felső")
    biztlef_nyomas = forms.DecimalField(required=True, label="Biztonsági lefúvató nyomás")
    diag_datum = forms.DateField(required=True, label="Diagnosztika dátum", widget=forms.TextInput(attrs={'class':'datum'}))
    #szabalyozo = forms.ModelChoiceField(queryset=Szabalyozok.objects.all(), empty_label="Kérem válasszon", required=True, label="Szabályozó")
    diagnosztikaok = forms.ModelChoiceField(queryset=DiagnosztikaOk.objects.all(), empty_label="Kérem válasszon", required=True, label="Diagnosztika oka")
    megjegyzes = forms.CharField(required=False, label="Megjegyzés", widget=forms.Textarea)


    class Meta(forms.ModelForm):
        model = Diagnosztika
        fields = ('p1_nyomas', 'p2_nyomas', 'p1_also_nyomas', 'p1_felso_nyomas', 'p2_also_nyomas', 'p2_felso_nyomas', 'biztlef_nyomas', 'diag_datum', 'diagnosztikaok', 'megjegyzes')
