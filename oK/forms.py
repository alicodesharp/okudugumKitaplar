from django import forms

class KitapForm(forms.Form):
    isim = forms.CharField(max_length=500)
    yazar = forms.CharField(max_length=500)
    konu = forms.CharField(max_length=500)
    notlarim = forms.CharField(max_length=1500)
    yayinevi = forms.CharField(max_length=500)
    okudugum_sene = forms.DateField()
    basim_yili = forms.DateField(required=False)
    pdf = forms.FileField(required=False)

