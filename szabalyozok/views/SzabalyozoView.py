from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# from datetime import datetime
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from szabalyozok.forms.DiagnosztikaForm import DiagnosztikaForm
from szabalyozok.forms.SzabalyozoForm import *
from szabalyozok.forms.MuszerForm import *
from szabalyozok.forms.TartozekokForm import *
from szabalyozok.forms.MunkaForm import *
from szabalyozok.forms.DocForm import *
from szabalyozok.forms.SzabingatlanForm import *
from szabalyozok.models import *
import json
import os
from django.conf import settings
from django.http import HttpResponse


def home(request):
    """Renders the about page."""
    form = SearchForm()
    return render(
        request,
        'szabalyozok/index.html',
        {
            'title': 'Szabalyozok', 'form': form,
        }
    )


def szabalyozok(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        form = SearchForm(request.POST)
        hiba = ''
        if form.is_valid():
            group = request.user.groups.values_list('name', flat=True).first()
            if group==None:
                group = 'admin'
            param = form.cleaned_data['search']
            szab = Szabalyozok.objects.filter((Q(allomas_nev__icontains=param) | Q(
                telepules__telepules__icontains=param) | Q(azonosito__icontains=param)) & Q(telepules__uzem__jog__contains=group))
            if len(szab) == 0:
                hiba = 'Nincs találat!'

            return render(request, 'szabalyozok/index.html',
                          {'title': 'Szabályozók', 'szabalyozok': szab, 'form': form, 'hiba': hiba, 'data': True})
    else:
        form = SearchForm()

    szab = ''  # Eszkoz.objects.all()
    return render(
        request,
        'szabalyozok/index.html',
        {
            'title': 'Szabályozók',
            'szabalyozok': szab,
            'form': form,
            'data': False
        }
    )


def szabterkep(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    gps_lat = szabalyozo.gps_lat
    gps_long = szabalyozo.gps_long
    szabnev = szabalyozo.allomas_nev
    return render(request, 'szabalyozok/szabterkep.html', {'gpslat': gps_lat, 'gpslong': gps_long, 'szabnev': szabnev})


def szabalyozo_show(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    diagnosz = Diagnosztika.objects.filter(szabalyozo_id=pk).order_by('diag_datum').reverse()[0:1]

    if len(diagnosz) != 0:
        diagnosztika = Diagnosztika.objects.get(pk=diagnosz)
        diag_p1 = diagnosztika.p1_nyomas
        diag_p2 = diagnosztika.p2_nyomas
    else:
        diag_p1 = 'Nincs megadva'
        diag_p2 = 'Nincs megadva'

    return render(request, 'szabalyozok/szabalyozo_show.html',
                  {'title': 'Szabályozó', 'szabalyozo': szabalyozo, 'diag_p1': diag_p1, 'diag_p2': diag_p2})


@login_required(login_url='/login/')
def szabalyozo_edit(request, pk):
    szab = get_object_or_404(Szabalyozok, pk=pk)
    if request.method == "POST":
        form = SzabalyozoForm(request.POST, instance=szab)
        if form.is_valid():
            szab = form.save(commit=False)
            szab.save()
            form.save_m2m()
            return redirect('szabalyozo_show', pk=pk)
    else:
        form = SzabalyozoForm(instance=szab)
    return render(request, 'szabalyozok/szabalyozo_edit.html', {'form': form})


def szabtart_show(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    szab_nev = szabalyozo.allomas_nev
    szab_id = szabalyozo.id
    tartozekok = Tartozekok.objects.filter(szabalyozo_id=pk).order_by('beszereles_datum').reverse()
    muszerek = Muszerek.objects.filter(szabalyozo_id=pk).order_by('beszereles_datum').reverse()
    return render(request, 'szabalyozok/szabtart_show.html',
                  {'title': 'Szabályozó tartozékok', 'szabnev': szab_nev, 'szabid': szab_id, 'tartozekok': tartozekok,
                   'muszerek': muszerek})


@login_required(login_url='/login/')
def tartozek_beki(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    szab_nev = szabalyozo.allomas_nev
    szab_id = szabalyozo.id
    tartozekok = Tartozekok.objects.filter(szabalyozo_id=pk).order_by('beszereles_datum').reverse()
    formki = TartozekkiszerelForm()

    # return HttpResponse(tartozekok, content_type="text/plain")
    return render(request, 'szabalyozok/tartozek_beki.html',
                  {'title': 'Szabályozó tartozékok', 'szabnev': szab_nev, 'szabid': szab_id, 'tartozekok': tartozekok,
                   'formki': formki})


@login_required(login_url='/login/')
def tartozek_ki(request, pk):
    szabid = pk
    if request.method == "POST":
        form = TartozekkiszerelForm(request.POST)
        if form.is_valid():
            kidatum = form.cleaned_data['kiszereles_datum']
            megjegyzes = form.cleaned_data['megjegyzes']
            tartozek_id = form.cleaned_data['tartozek']

            szabalyozo = get_object_or_404(Szabalyozok, pk=szabid)
            szab_id = szabalyozo.id
            tartozek = get_object_or_404(Tartozekok, pk=tartozek_id)
            bedatum = tartozek.beszereles_datum
            tartozek.szabalyozo_id = None
            tartozek.save()

            tartozekki = Tartozekkiszerel(beszereles_datum=bedatum, kiszereles_datum=kidatum, szabalyozo_id=szab_id, tartozek_id=tartozek_id, megjegyzes=megjegyzes)
            tartozekki.save()

            # return redirect('tartozek_beki', pk=pk)
    return redirect('tartozek_beki', pk=pk)

# @login_required(login_url='/login/')
# def tartozek_ki(request, pk):
#     szabid = pk
#     if request.method == "POST":
#         form = TartozekkiszerelForm(request.POST)
#         if form.is_valid():
#             tartozekki = form.save(commit=False)
#             szabalyozo = Szabalyozok.objects.get(id=szabid)
#             tartozekki.szabalyozo = szabalyozo
#             tartozekki.beszereles_datum = tartozekki.tartozek.beszereles_datum
#             tartozekid = tartozekki.tartozek.id
#             tartozek = Tartozekok.objects.get(id=tartozekid)
#             tartozek.szabalyozo_id = ""
#
#             tartozekki.save()
#             tartozek.save()
#             return redirect('tartozek_beki', pk=pk)
#     return redirect('tartozek_beki', pk=pk)



@login_required(login_url='/login/')
def tartozek_new(request, pk):
    if request.method == "POST":
        form = TartozekForm(request.POST)
        if form.is_valid():
            tart = form.save(commit=False)
            tart.szabalyozo_id = pk
            tart.save()
            return redirect('tartozek_beki', pk=pk)
    else:
        form = TartozekForm()
    return render(request, 'szabalyozok/tartozek_new.html', {'form': form})


@login_required(login_url='/login/')
def tartozek_edit(request, pk, spk):
    tartozek = get_object_or_404(Tartozekok, pk=pk)
    fajta = tartozek.tartozektipus.tartozekfajta
    gyarto = tartozek.tartozektipus.tartozekgyarto

    if request.method == "POST":
        form = TartozekForm(request.POST, instance=tartozek, initial={'tartozekfajta': fajta, 'tartozekgyarto': gyarto})
        if form.is_valid():
            form.save()
            return redirect('tartozek_beki', pk=spk)
    else:
        form = TartozekForm(instance=tartozek, initial={'tartozekfajta': fajta, 'tartozekgyarto': gyarto})
    return render(request, 'szabalyozok/tartozek_edit.html', {'form': form})


def tartozek_tortenet(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    szab_nev = szabalyozo.allomas_nev
    szab_id = szabalyozo.id
    tartozek_tortenet = Tartozekkiszerel.objects.filter(szabalyozo_id=pk).order_by('kiszereles_datum').reverse()[0:15]
    hiba = ''
    if len(tartozek_tortenet) == 0:
        hiba = 'Nincs találat!'
    return render(request, 'szabalyozok/szabtart_tortenet.html',
                  {'title': 'Szabályozó tartozék történek', 'szabnev': szab_nev, 'szabid': szab_id,
                   'tartozekok': tartozek_tortenet, 'hiba': hiba})


@login_required(login_url='/login/')
def muszer_beki(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    szab_nev = szabalyozo.allomas_nev
    szab_id = szabalyozo.id
    muszerek = Muszerek.objects.filter(szabalyozo_id=pk).order_by('beszereles_datum').reverse()
    formki = MuszerkiszerelForm()
    form = MuszerSearchForm()
    hiba = ''
    muszersearch = ''
    if request.method == "POST":
        form = MuszerSearchForm(request.POST)
        if form.is_valid():
            param = form.cleaned_data['search']
            muszersearch = Muszerek.objects.filter(gyariszam__icontains=param, selejt=False)
            if len(muszersearch) == 0:
                hiba = 'Nincs találat!'
                return render(request, 'szabalyozok/muszer_beki.html',
                              {'title': 'Szabályozó műszerek', 'szabnev': szab_nev, 'szabid': szab_id,
                               'muszerek': muszerek, 'formki': formki, 'form': form, 'hiba': hiba,
                               'muszersearch': muszersearch})

    return render(request, 'szabalyozok/muszer_beki.html',
                  {'title': 'Szabályozó műszerek', 'szabnev': szab_nev, 'szabid': szab_id,
                   'muszerek': muszerek, 'formki': formki, 'form': form, 'hiba': hiba, 'muszersearch': muszersearch})


@login_required(login_url='/login/')
def muszer_ki(request, pk):
    szabid = pk
    if request.method == "POST":
        form = MuszerkiszerelForm(request.POST)
        if form.is_valid():
            kidatum = form.cleaned_data['kiszereles_datum']
            megjegyzes = form.cleaned_data['megjegyzes']
            muszer_id = form.cleaned_data['muszer']
            selejt = form.cleaned_data['selejt']

            szabalyozo = get_object_or_404(Szabalyozok, pk=szabid)
            szab_id = szabalyozo.id

            muszer = get_object_or_404(Muszerek, pk=muszer_id)
            bedatum = muszer.beszereles_datum
            muszer.szabalyozo_id = None
            muszer.jegyzokonyv_szam = None
            muszer.kalib_datum = None
            muszer.kov_kalib_datum = None
            muszer.beszereles_datum = None
            muszer.elhelyezkedes = None
            if selejt:
                muszer.selejt = True
            muszer.save()

            muszerki = Muszerkiszerel(beszereles_datum=bedatum, kiszereles_datum=kidatum, szabalyozo_id=szab_id, muszer_id=muszer_id, megjegyzes=megjegyzes, selejt=selejt)
            muszerki.save()
    return redirect('muszer_beki', pk=pk)


@login_required(login_url='/login/')
def muszer_be(request, pk, spk):
    muszerid = pk
    szabid = spk
    muszer = get_object_or_404(Muszerek, pk=muszerid)
    if request.method == "POST":
        form = MuszerbeszerelForm(request.POST, instance=muszer)
        if form.is_valid():
            muszerbe = form.save(commit=False)
            muszer.szabalyozo_id = szabid
            muszerbe.save()
            return redirect('muszer_beki', pk=szabid)
    else:
        form = MuszerbeszerelForm(instance=muszer)
    return render(request, 'szabalyozok/muszer_be.html', {'form': form})


def muszer_tortenet(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    szab_nev = szabalyozo.allomas_nev
    szab_id = szabalyozo.id
    muszer_tortenet = Muszerkiszerel.objects.filter(szabalyozo_id=pk).order_by('kiszereles_datum').reverse()[0:15]
    hiba = ''
    if len(muszer_tortenet) == 0:
        hiba = 'Nincs találat!'
    return render(request, 'szabalyozok/muszer_tortenet.html',
                  {'title': 'Szabályozó műszer történek', 'szabnev': szab_nev, 'szabid': szab_id,
                   'muszerek': muszer_tortenet, 'hiba': hiba})


@login_required(login_url='/login/')
def manometernew(request):
    if request.method == "POST":
        form = ManometernewForm(request.POST)
        if form.is_valid():
            manometer = form.save(commit=False)
            manometer.selejt = False
            manometer.save()
            return render(request, 'szabalyozok/manometer_new.html', {'form': form, 'siker': 'Manométer feltöltve! '})
    else:
        form = ManometernewForm()
    return render(request, 'szabalyozok/manometer_new.html', {'form': form})


@login_required(login_url='/login/')
def manometer_edit(request, pk):
    manometer = get_object_or_404(Muszerek, pk=pk)
    if request.method == "POST":
        form = ManometernewForm(request.POST, instance=manometer)
        if manometer.muszertipus.muszerfajta.id == 1:
            if form.is_valid():
                form.save()
                return redirect('riport_muszerek_api')
        else:
            return HttpResponse('Valami gubanc van!!!', content_type="text/plain")
    else:
        form = ManometernewForm(instance=manometer)
    return render(request, 'szabalyozok/manometer_edit.html', {'form': form})


@login_required(login_url='/login/')
def szabmunka_show(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    szab_nev = szabalyozo.allomas_nev
    szab_id = szabalyozo.id
    szabmunkak = Szabalyozomunkak.objects.filter(szabalyozo_id=szab_id).order_by('szabmunka_datum').reverse()
    return render(request, 'szabalyozok/szabmunkak_show.html',
                  {'title': 'Szabályozó munkák', 'szabnev': szab_nev, 'szabid': szab_id, 'szabmunkak': szabmunkak})


@login_required(login_url='/login/')
def szabmunka_new(request, pk):
    if request.method == "POST":
        form = SzabalyozoMunkaForm(request.POST)
        if form.is_valid():
            szabmunka = form.save(commit=False)
            szabmunka.szabalyozo_id = pk
            szabmunka.save()
            return redirect('szabmunka_show', pk=pk)
    else:
        form = SzabalyozoMunkaForm()
    return render(request, 'szabalyozok/szabmunkak_new.html', {'form': form})


@login_required(login_url='/login/')
def szabmunka_edit(request, pk, spk):
    munkaid = pk
    szabid = spk
    szabmunka = get_object_or_404(Szabalyozomunkak, pk=munkaid)
    if request.method == "POST":
        form = SzabalyozoMunkaForm(request.POST, instance=szabmunka)
        if form.is_valid():
            szmunka = form.save(commit=False)
            szmunka.szabalyozo_id = szabid
            szmunka.save()
            return redirect('szabmunka_show', pk=szabid)
    else:
        form = SzabalyozoMunkaForm(instance=szabmunka)
    return render(request, 'szabalyozok/szabmunkak_edit.html', {'form': form})


@login_required(login_url='/login/')
def muszermunka_show(request, pk, spk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=spk)
    muszer = get_object_or_404(Muszerek, pk=pk)
    szab_id = szabalyozo.id
    muszer_id = muszer.id
    muszer_nev = muszer.muszertipus
    muszermunkak = Muszermunkak.objects.filter(muszer_id=muszer_id).order_by('muszmunka_datum').reverse()
    return render(request, 'szabalyozok/muszermunkak_show.html',
                  {'title': 'Műszer munkák', 'szabid': szab_id, 'muszerid': muszer_id, 'muszernev': muszer_nev,
                   'muszermunkak': muszermunkak})


@login_required(login_url='/login/')
def muszermunka_new(request, pk, spk):
    if request.method == "POST":
        form = MuszerMunkaForm(request.POST)
        if form.is_valid():
            muszermunka = form.save(commit=False)
            muszermunka.muszer_id = pk
            muszermunka.save()
            return redirect('muszermunka_show', pk=pk, spk=spk)
    else:
        form = MuszerMunkaForm()
    return render(request, 'szabalyozok/muszermunkak_new.html', {'form': form})


@login_required(login_url='/login/')
def muszermunka_edit(request, pk, mpk, spk):
    munkaid = pk
    muszerid = mpk
    szabid = spk
    muszermunka = get_object_or_404(Muszermunkak, pk=munkaid)
    if request.method == "POST":
        form = MuszerMunkaForm(request.POST, instance=muszermunka)
        if form.is_valid():
            muszmunka = form.save(commit=False)
            muszmunka.szabalyozo_id = szabid
            muszmunka.save()
            return redirect('muszermunka_show', pk=muszerid, spk=szabid)
    else:
        form = MuszerMunkaForm(instance=muszermunka)
    return render(request, 'szabalyozok/muszermmunkak_edit.html', {'form': form})


@login_required(login_url='/login/')
def doc_list(request, tip, eszid, spk):
    eszkoz_nev = ''
    doc_list = Doc.objects.filter(doctipus=tip, eszkoz_id=eszid).order_by('felt_datum').reverse()

    if tip == 'szab':
        eszkoz = Szabalyozok.objects.get(id=eszid)
        eszkoz_nev = eszkoz.allomas_nev
    elif tip == 'muszer':
        eszkoz = Muszerek.objects.get(id=eszid)
        eszkoz_nev = eszkoz.muszertipus
    elif tip == 'szabmunkak':
        eszkoz = Szabalyozomunkak.objects.get(id=eszid)
        eszkoz_nev = eszkoz.szabalyozomunkatipus
    elif tip == 'muszermunkak':
        eszkoz = Muszermunkak.objects.get(id=eszid)
        eszkoz_nev = eszkoz.muszermunkatipus

    return render(request, 'szabalyozok/doc_list.html',
                  {'title': 'Dokumentumok', 'doclist': doc_list, 'szabid': spk, 'tipus': tip, 'eszid': eszid,
                   'eszkoznev': eszkoz_nev})


@login_required(login_url='/login/')
def doc_new(request, tip, eszid, spk):
    if request.method == "POST":
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            today = timezone.now()
            doc.doctipus = tip
            doc.eszkoz_id = eszid
            doc.felt_datum = today
            doc.save()
            return redirect('doc_list', tip=tip, eszid=eszid, spk=spk)
    else:
        form = DocForm()
    return render(request, 'szabalyozok/doc_new.html', {'form': form})


@login_required(login_url='/login/')
def doc_del(request, tip, pk, eszid, spk):
    doksi = Doc.objects.get(id=pk)
    docnev = str(doksi.docfile)
    doksi.delete()

    try:
        os.remove(os.path.join(settings.MEDIA_ROOT, docnev))

    except ValueError:
        print("Valami gáz van...")

    return redirect('doc_list', tip=tip, eszid=eszid, spk=spk)


def kep_list(request, spk):
    szab = Szabalyozok.objects.get(id=spk)
    szab_nev = szab.allomas_nev
    kep_list = Image.objects.filter(szabalyozo_id=spk)

    return render(request, 'szabalyozok/kep_list.html',
                  {'title': 'Képek', 'keplist': kep_list, 'szabid': spk, 'szabnev': szab_nev})


@login_required(login_url='/login/')
def kep_new(request, spk):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            kep = form.save(commit=False)
            kep.szabalyozo_id = spk
            kep.save()
            return redirect('kep_list', spk=spk)
    else:
        form = ImageForm()
    return render(request, 'szabalyozok/kep_new.html', {'form': form})


@login_required(login_url='/login/')
def kep_del(request, pk, spk):
    kep = Image.objects.get(id=pk)
    kepnev = str(kep.image)
    kep.delete()
    a, b = kepnev.split(".")

    try:
        os.remove(os.path.join(settings.MEDIA_ROOT, kepnev))
        os.remove(os.path.join(settings.MEDIA_ROOT, a + ".normal." + b))
        os.remove(os.path.join(settings.MEDIA_ROOT, a + ".thumbnail." + b))

    except ValueError:
        print("Valami gáz van...")

    return redirect('kep_list', spk=spk)


def diagnosztika(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    diagnosztika = Diagnosztika.objects.filter(szabalyozo_id=pk).order_by('diag_datum').reverse()[0:1]
    szabnev = szabalyozo.allomas_nev

    return render(request, 'szabalyozok/diagnosztika.html',
                  {'szabnev': szabnev, 'szabid': pk, 'diagnosztika': diagnosztika})


def diagnosztika_tortenet(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    diagnosztika = Diagnosztika.objects.filter(szabalyozo_id=pk).order_by('diag_datum').reverse()[1:15]
    szabnev = szabalyozo.allomas_nev

    return render(request, 'szabalyozok/diagnosztika_tortenet.html',
                  {'szabnev': szabnev, 'szabid': pk, 'diagnosztika': diagnosztika})


@login_required(login_url='/login/')
def diagnosztika_new(request, pk):
    if request.method == "POST":
        form = DiagnosztikaForm(request.POST)
        if form.is_valid():
            diag = form.save(commit=False)
            diag.szabalyozo_id = pk
            diag.diag_felvitel = timezone.now()
            diag.save()

            # utolsó diagnosztikai keresés
            last_diag = Diagnosztika.objects.filter(szabalyozo_id=pk).order_by('diag_datum').reverse()[0:1].get()
            p1_nyomas = last_diag.p1_nyomas
            p2_nyomas = last_diag.p2_nyomas

            # utolsó diagnosztikai p1, p2 nyomás visszaírása a szab. táblába
            szabalyozo = Szabalyozok.objects.get(id=pk)
            szabalyozo.uz_prim_nyom = p1_nyomas
            szabalyozo.uz_sek_nyom = p2_nyomas
            szabalyozo.save()

            return redirect('diagnosztika', pk=pk)
    else:
        form = DiagnosztikaForm()
    return render(request, 'szabalyozok/diagnosztika_new.html', {'form': form})


def terkep(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    fogadok = Szabalyozok.objects.filter(funkcio='fogado', telepules__uzem__jog__contains=group).values('id', 'allomas_nev', 'gps_lat', 'gps_long', 'uz_prim_nyom', 'uz_sek_nyom')
    korzeti = Szabalyozok.objects.filter(funkcio='korzeti', telepules__uzem__jog__contains=group).values('id', 'allomas_nev', 'gps_lat', 'gps_long', 'uz_prim_nyom', 'uz_sek_nyom')
    egyeb = Szabalyozok.objects.filter(Q(telepules__uzem__jog__contains=group) & ~Q(funkcio='fogado') & ~Q(funkcio='korzeti')).values('id', 'allomas_nev',
                                                                                            'gps_lat', 'gps_long', 'uz_prim_nyom', 'uz_sek_nyom')
    fogado_seri = json.dumps(list(fogadok), ensure_ascii=False, cls=DjangoJSONEncoder)
    korzeti_seri = json.dumps(list(korzeti), ensure_ascii=False, cls=DjangoJSONEncoder)
    egyeb_seri = json.dumps(list(egyeb), ensure_ascii=False, cls=DjangoJSONEncoder)

    with open(os.path.join(settings.MEDIA_ROOT, 'json/fogadok.json'), 'w', encoding='utf-8') as outfile:
        outfile.write(fogado_seri)

    with open(os.path.join(settings.MEDIA_ROOT, 'json/korzetik.json'), 'w', encoding='utf-8') as outfile:
        outfile.write(korzeti_seri)

    with open(os.path.join(settings.MEDIA_ROOT, 'json/egyeb.json'), 'w', encoding='utf-8') as outfile:
        outfile.write(egyeb_seri)

    return render(request, 'szabalyozok/terkep.html')


# def get_tartozekgyarto(request, pk):
#     fajta = get_object_or_404(Tartozekfajta, pk=pk)
#     gyarto = Tartozekgyartok.objects.all().values('id', 'tartozekgyarto').order_by('tartozekgyarto')
#     gyartok = json.dumps(list(gyarto), ensure_ascii=False, cls=DjangoJSONEncoder)
#     # return HttpResponse(gyartok, content_type="text/plain")
#     return HttpResponse(gyartok, content_type="application/json")


def get_tartozektipus(request, fpk, gpk):
    fajta = get_object_or_404(Tartozekfajta, pk=fpk)
    gyarto = get_object_or_404(Tartozekgyartok, pk=gpk)

    tipus = Tartozektipus.objects.filter(tartozekfajta_id=fajta.id, tartozekgyarto_id=gyarto.id).values('id', 'tartozektipus').order_by('tartozektipus')
    tipusok = json.dumps(list(tipus), ensure_ascii=False, cls=DjangoJSONEncoder)
    return HttpResponse(tipusok, content_type="application/json")
    # return HttpResponse(tipusok, content_type="text/plain")


@login_required(login_url='/login/')
def szabingatlan_show(request, pk):
    szabalyozo = get_object_or_404(Szabalyozok, pk=pk)
    szab_nev = szabalyozo.allomas_nev
    szab_id = szabalyozo.id
    szabingatlan = SzabalyozokIngatlan.objects.filter(szabalyozo=szabalyozo)
    return render(request, 'szabalyozok/szabingatlan_show.html',
                  {'title': 'Szabályozó ingatlan', 'szabnev': szab_nev, 'szabid': szab_id, 'szabingatlan': szabingatlan})


@login_required(login_url='/login/')
def szabingatlan_edit(request, pk):
    szabingatlan = get_object_or_404(SzabalyozokIngatlan, pk=pk)
    if request.method == "POST":
        form = SzabIngatlanForm(request.POST, instance=szabingatlan)
        if form.is_valid():
            form.save()
            return redirect('riport_szabingatlan')
    else:
        form = SzabIngatlanForm(instance=szabingatlan)
    return render(request, 'szabalyozok/szabingatlan_edit.html', {'form': form})


@login_required(login_url='/login/')
def szabingatlan_new(request):
    if request.method == "POST":
        form = SzabIngatlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('riport_szabingatlan')
    else:
        form = SzabIngatlanForm()
    return render(request, 'szabalyozok/szabingatlan_new.html', {'form': form})


@login_required(login_url='/login/')
def szabingatlan_edit_szab(request, pk, spk):
    szabingatlan = get_object_or_404(SzabalyozokIngatlan, pk=pk)
    if request.method == "POST":
        form = SzabIngatlanForm(request.POST, instance=szabingatlan)
        if form.is_valid():
            form.save()
            return redirect('szabingatlan_show', pk=spk)
    else:
        form = SzabIngatlanForm(instance=szabingatlan)
    return render(request, 'szabalyozok/szabingatlan_edit.html', {'form': form})