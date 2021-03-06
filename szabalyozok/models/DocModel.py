import datetime
import hashlib
import os
from django.db import models
from stdimage.models import StdImageField
from szabalyozok.models import SzabalyozoModel

class Dockategoria(models.Model):
    dockategoria = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Dokumentum kategória"
        ordering = ('dockategoria',)

    def __str__(self):
        return self.dockategoria


def content_file_name(instance, filename):
    now = datetime.datetime.now()
    ev = str(now.year)
    ho = str(now.month)
    ext = filename.split('.')[-1]
    filename = "%s_%s" % (instance.doc_nev, now )
    md5 = hashlib.md5(filename.encode('utf-8')).hexdigest()
    filenamemd5 = "%s.%s" % (md5, ext)
    return os.path.join('documents/' + ev + '/' + ho, filenamemd5)


class Doc(models.Model):
    doctipus = models.CharField(max_length=20, blank=False, null=False)
    eszkoz_id = models.IntegerField(blank=False, null=False)
    felt_datum = models.DateField(blank=False, null=False)
    doc_nev = models.CharField(max_length=200, blank=False, null=False)
    dockategoria = models.ForeignKey(Dockategoria, blank=True, null=True)
    docfile = models.FileField(upload_to=content_file_name)

    class Meta:
        verbose_name_plural = "Dokumentumok"

    def __str__(self):
        return self.doc_nev

def content_kep_name(instance, filename):
    now = datetime.datetime.now()
    ev = str(now.year)
    ho = str(now.month)
    ext = filename.split('.')[-1]
    filename = "%s_%s" % (instance.image_nev, now )
    md5 = hashlib.md5(filename.encode('utf-8')).hexdigest()
    filenamemd5 = "%s.%s" % (md5, ext)
    return os.path.join('kepek/' + ev + '/' + ho, filenamemd5)

class Image(models.Model):
    image_nev = models.CharField(max_length=200, blank=False, null=False)
    szabalyozo = models.ForeignKey(SzabalyozoModel.Szabalyozok, blank=True, null=True)
    image = StdImageField(upload_to=content_kep_name,
                          variations={'normal': (1024, 768), 'thumbnail': (100, 75), })

    class Meta:
        verbose_name_plural = "Képek"

    def __str__(self):
        return self.image_nev