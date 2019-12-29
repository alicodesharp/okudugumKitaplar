from django.shortcuts import render
from oK.models import *
from django.views.generic import FormView
from oK.forms import *

# Create your views here.

class Okudugum_Kitaplar(FormView):
    template_name = "Anasayfa.html"
    form_class = KitapForm
    success_url = "/"

    def form_valid(self, form):
        Kitaplar.objects.create(
            isim=form.cleaned_data["isim"],
            yazar=form.cleaned_data["yazar"],
            konu=form.cleaned_data["konu"],
            notlarim=form.cleaned_data["notlarim"],
            yayinevi= form.cleaned_data["yayinevi"],
            okudugum_sene=form.cleaned_data["okudugum_sene"],
            basim_yili=form.cleaned_data["basim_yili"],
            pdf = self.request.FILES["pdf"]
        )
        return super(Okudugum_Kitaplar, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Okudugum_Kitaplar, self).get_context_data(**kwargs)
        context["kitaplarim"] = Kitaplar.objects.all().order_by("-eklenme_tarihi")
        return context
