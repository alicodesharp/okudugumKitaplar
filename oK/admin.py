from django.contrib import admin
from oK.models import *
# Register your models here.

class KitaplarAdmin(admin.ModelAdmin):
    list_display = ["isim","yazar","okudugum_sene"]
    list_filter = ["okudugum_sene","yazar"]




admin.site.register(Kitaplar,KitaplarAdmin)
