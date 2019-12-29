from django.db import models


# Create your models here.
class Kitaplar(models.Model):
    isim = models.CharField(max_length=500)
    yazar = models.CharField(max_length=500)
    konu = models.CharField(max_length=500)
    notlarim = models.CharField(max_length=1500)
    yayinevi = models.CharField(max_length=500)
    okudugum_sene = models.DateField()
    basim_yili = models.DateField(null=True,blank=True)
    pdf = models.FileField(upload_to="myBooks",null=True,blank=True)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Kitaplarım"

    def __str__(self):
        return self.isim


