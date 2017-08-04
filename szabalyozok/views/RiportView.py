# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.views.decorators.cache import cache_page
from szabalyozok.models import *
from szabalyozok.forms.DocForm import *
from django.http import HttpResponse
import itertools
from django.core.serializers.json import DjangoJSONEncoder
import json


# @cache_page(60 * 15)
@login_required(login_url='/login/')
def riport_szabalyozok(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    szabalyozok = SzabalyozokRiport.objects.filter(jog__contains=group)

    # return HttpResponse(group, content_type="text/plain")
    return render(
        request,
        'szabalyozok/riport_szabalyozok.html',
        {
            'title': 'Szabalyozok',
            'szabalyozok': szabalyozok,
        }
    )


@login_required(login_url='/login/')
def riport_szabtartozekok(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    szabtartozekok = TartozekRiport.objects.filter(jog__contains=group)

    return render(
        request,
        'szabalyozok/riport_szabtartozekok.html',
        {
            'title': 'Tartozékok',
            'szabtartozekok': szabtartozekok,
        }
    )


@login_required(login_url='/login/')
def riport_diagnosztika(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    diagnosztikak = DiagnosztikaRiport.objects.filter(jog__contains=group)

    return render(
        request,
        'szabalyozok/riport_diagnosztikak.html',
        {
            'title': 'Diagnosztikák',
            'diagnosztikak': diagnosztikak,
        }
    )


@login_required(login_url='/login/')
def riport_muszerek(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    muszerek_be = MuszerRiport.objects.filter(jog__contains=group)
    muszerek_ki = MuszerRiport.objects.filter(szab_id=None)
    muszerek = itertools.chain(muszerek_be, muszerek_ki)

    return render(
        request,
        'szabalyozok/riport_muszerek.html',
        {
            'title': 'Muszerek',
            'muszerek': muszerek,
        }
    )


@login_required(login_url='/login/')
def riport_muszermunkak(request):
    # group = request.user.groups.values_list('name', flat=True).first()
    # if group == None:
    #     group = 'admin'
    muszermunkak = MuszermunkaRiport.objects.all()

    return render(
        request,
        'szabalyozok/riport_muszermunkak.html',
        {
            'title': 'Szabályozó munkák',
            'muszermunkak': muszermunkak,
        }
    )


@login_required(login_url='/login/')
def riport_szabmunkak(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    szabmunkak = SzabmunkakRiport.objects.filter(jog__contains=group)

    return render(
        request,
        'szabalyozok/riport_szabmunkak.html',
        {
            'title': 'Szabályozó munkák',
            'szabmunkak': szabmunkak,
        }
    )


@login_required(login_url='/login/')
def simple_doc_list(request, tip, eszid):
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

    return render(request, 'szabalyozok/simple_doc_list.html',
                  {'title': 'Dokumentumok', 'doclist': doc_list, 'tipus': tip, 'eszid': eszid,
                   'eszkoznev': eszkoz_nev})


# ------ Új riport apik ------

@login_required(login_url='/login/')
def riport_szabalyozok_api(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    szabalyozok_list = SzabalyozokRiport.objects.filter(jog__contains=group).values()

    szabalyozok = json.dumps(list(szabalyozok_list), ensure_ascii=False, cls=DjangoJSONEncoder)

    # return HttpResponse(szabalyozok, content_type="text/plain")
    return render(
        request,
        'szabalyozok/riport_szabalyozokapi.html',
        {
            'title': 'Szabalyozok',
            'szabalyozok': szabalyozok,
        }
    )


@login_required(login_url='/login/')
def riport_szabtartozekok_api(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    szabalyozok_list = TartozekRiport.objects.filter(jog__contains=group).values()
    szabalyozok = json.dumps(list(szabalyozok_list), ensure_ascii=False, cls=DjangoJSONEncoder)

    # return HttpResponse(szabalyozok, content_type="text/plain")
    return render(
        request,
        'szabalyozok/riport_tartozekapi.html',
        {
            'title': 'Szabalyozok',
            'tartozekok': szabalyozok,
        }
    )


@login_required(login_url='/login/')
def riport_muszerek_api(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    muszerek_be = MuszerRiport.objects.filter(jog__contains=group).values()
    muszerek_ki = MuszerRiport.objects.filter(szab_id=None).values()
    muszerek_ossz = itertools.chain(muszerek_be, muszerek_ki)
    muszerek = json.dumps(list(muszerek_ossz), ensure_ascii=False, cls=DjangoJSONEncoder)

    return render(
        request,
        'szabalyozok/riport_muszerekapi.html',
        {
            'title': 'Muszerek',
            'muszerek': muszerek,
        }
    )


@login_required(login_url='/login/')
def riport_diagnosztika_api(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    diagnosztikak_list = DiagnosztikaRiport.objects.filter(jog__contains=group).values()
    diagnosztikak = json.dumps(list(diagnosztikak_list), ensure_ascii=False, cls=DjangoJSONEncoder)

    return render(
        request,
        'szabalyozok/riport_diagnosztikakapi.html',
        {
            'title': 'Diagnosztikák',
            'diagnosztikak': diagnosztikak,
        }
    )


@login_required(login_url='/login/')
def riport_szabmunkak_api(request):
    group = request.user.groups.values_list('name', flat=True).first()
    if group == None:
        group = 'admin'
    szabmunkak_list = SzabmunkakRiport.objects.filter(jog__contains=group).values()
    szabmunkak = json.dumps(list(szabmunkak_list), ensure_ascii=False, cls=DjangoJSONEncoder)

    return render(
        request,
        'szabalyozok/riport_szabmunkakapi.html',
        {
            'title': 'Szabályozó munkák',
            'szabmunkak': szabmunkak,
        }
    )


@login_required(login_url='/login/')
def riport_muszermunkak_api(request):
    muszermunkak_list = MuszermunkaRiport.objects.all().values()
    muszermunkak = json.dumps(list(muszermunkak_list), ensure_ascii=False, cls=DjangoJSONEncoder)

    return render(
        request,
        'szabalyozok/riport_muszermunkakapi.html',
        {
            'title': 'Szabályozó munkák',
            'muszermunkak': muszermunkak,
        }
    )


def riport_dokumentumfilter(request):
    if request.method == "POST":
        form = DocFilterForm(request.POST)
        if form.is_valid():
            hiba = ''
            doktipus = form.cleaned_data['doktipus']
            kat_param = request.POST.get('dockategoria')

            # if kat_param == '':
            #     kat_param = form.cleaned_data['dockategoria']  # IS NULL
            # else:
            #     int(kat_param)

            if kat_param != '':
                int(kat_param)

            kez_datum = form.cleaned_data['kez_datum']
            veg_datum = form.cleaned_data['veg_datum']

            if kez_datum == None:
                kez_datum = '1950-01-01'

            if veg_datum == None:
                veg_datum = '2050-01-01'

            # return HttpResponse(kez_datum, content_type="text/plain")

            if kat_param == '':   # Összes dockategória
                if doktipus == 'szab':
                    dok = Dok_Szabalyozo_Riport.objects.filter(felt_datum__range=(kez_datum, veg_datum)).values()
                elif doktipus == 'muszer':
                    dok = Dok_Muszer_Riport.objects.filter(felt_datum__range=(kez_datum, veg_datum)).values()
                elif doktipus == 'szabmunkak':
                    dok = Dok_Szabalyozo_Munka_Riport.objects.filter(felt_datum__range=(kez_datum, veg_datum)).values()
                elif doktipus == 'muszermunkak':
                    dok = Dok_Muszer_Munka_Riport.objects.filter(felt_datum__range=(kez_datum, veg_datum)).values()
                else:
                    dok = ''
            else:
                if doktipus == 'szab':
                    dok = Dok_Szabalyozo_Riport.objects.filter(dockategoria_id=kat_param, felt_datum__range=(kez_datum, veg_datum)).values()
                elif doktipus == 'muszer':
                    dok = Dok_Muszer_Riport.objects.filter(dockategoria_id=kat_param, felt_datum__range=(kez_datum, veg_datum)).values()
                elif doktipus == 'szabmunkak':
                    dok = Dok_Szabalyozo_Munka_Riport.objects.filter(dockategoria_id=kat_param, felt_datum__range=(kez_datum, veg_datum)).values()
                elif doktipus == 'muszermunkak':
                    dok = Dok_Muszer_Munka_Riport.objects.filter(dockategoria_id=kat_param, felt_datum__range=(kez_datum, veg_datum)).values()
                else:
                    dok = ''

            doklist = json.dumps(list(dok), ensure_ascii=False, cls=DjangoJSONEncoder)

            if len(doklist) == 0:
                hiba = 'Nincs találat!'

            return render(request, 'szabalyozok/riport_dokumentumok.html', {'title': 'Dokumentum riport', 'doklist': doklist, 'hiba': hiba})
            # return HttpResponse(doklist, content_type="text/plain")
    else:
        form = DocFilterForm()

    return render(
        request,
        'szabalyozok/riport_dokumentumok_filter.html',
        {
            'title': 'Dokumentum riport választó',
            'form': form,
        }
    )