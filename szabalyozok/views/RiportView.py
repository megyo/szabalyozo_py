from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.views.decorators.cache import cache_page
from szabalyozok.models import *
# from django.http import HttpResponse
import itertools


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
