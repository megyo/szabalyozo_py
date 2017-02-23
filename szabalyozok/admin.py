from django.contrib import admin
from .models import *


#Szabályozók admin
class SzabalyozokAdmin(admin.ModelAdmin):
    list_display = ('azonosito','telepules','allomas_nev')
    # exclude = ('uz_prim_nyom', 'uz_sek_nyom')
    # list_filter = [sz.name for sz in Szabalyozok._meta.fields]
    search_fields = ('allomas_nev',)


class TartozektipusokAdmin(admin.ModelAdmin):
    list_display = ('tartozektipus', 'tartozekfajta','tartozekgyarto')
    list_filter = ('tartozekfajta','tartozekgyarto')
    search_fields = ('tartozektipus',)


class TartozekokAdmin(admin.ModelAdmin):
    def tartozekfajta(self, instance):
        return instance.tartozektipus.tartozekfajta

    def tartozekgyarto(self, instance):
        return instance.tartozektipus.tartozekgyarto

    list_display = ('tartozektipus', 'tartozekfajta', 'tartozekgyarto', 'szabalyozo')
    # list_filter = ('tartozekgyarto','tartozektipus')
    search_fields = ('szabalyozo',)


class MuszertipusAdmin(admin.ModelAdmin):
    def muszerfajta(self, instance):
        return instance.muszertipus.muszerfajta

    def muszergyarto(self, instance):
        return instance.muszertipus.muszergyarto

    list_display = ('muszertipus', 'muszerfajta', 'muszergyarto')
    # list_filter = ('tartozekgyarto','tartozektipus')
    search_fields = ('muszertipus',)


class MuszerekAdmin(admin.ModelAdmin):
    list_display = ('muszertipus','gyariszam','szabalyozo')
    # list_filter = ('muszertipus','muszerfajta')
    search_fields = ('gyariszam',)


class DiagnosztikaAdmin(admin.ModelAdmin):
    def szabalyozo__telepules(self, obj):
        return obj.szabalyozo.telepules

    #szabalyozo__telepules = lambda s, o: o.szabalyozo.telepules
    list_display = ('diagnosztikaok','szabalyozo','szabalyozo__telepules','diag_datum')
    list_filter = ('diagnosztikaok',)
    search_fields = ('szabalyozo__allomas_nev',)


admin.site.register(Szabalyozok, SzabalyozokAdmin)
admin.site.register(SzabVezerlesMod)
admin.site.register(SzabKarb)
admin.site.register(EllenorzesiCiklus)
admin.site.register(DiagnosztikaOk)
admin.site.register(Diagnosztika, DiagnosztikaAdmin)
#admin.site.register(Atadok)
#admin.site.register(Telepulesek)
#admin.site.register(Uzemek)
#admin.site.register(Megyek)
admin.site.register(Tartozekgyartok)

#Tartozékok admin
admin.site.register(Tartozekfajta)
admin.site.register(Tartozektipus, TartozektipusokAdmin)
admin.site.register(Tartozekok, TartozekokAdmin)

#Műszerek admin
admin.site.register(Muszerfajta)
admin.site.register(Muszertipus, MuszertipusAdmin)
admin.site.register(Muszergyarto)
admin.site.register(Muszerek, MuszerekAdmin)
#admin.site.register(Muszerkiszerel)

#Munkák admin
#admin.site.register(Muszermunkak)
#admin.site.register(Szabalyozomunkak)
admin.site.register(MuszerMunkatipus)
admin.site.register(SzabalyozoMunkatipus)
#admin.site.register(Image)


