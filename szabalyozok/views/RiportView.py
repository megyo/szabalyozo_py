from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from szabalyozok.models import *


@login_required(login_url='/login/')
def riport_szabmunkak(request):
    szabmunkak = Szabalyozomunkak.objects.all()
    return render(
        request,
        'szabalyozok/riport_szabmunkak.html',
        {
            'title': 'Szabályozó munkák',
            'szabmunkak': szabmunkak,
        }
    )


@login_required(login_url='/login/')
def riport_muszermunkak(request):
    muszermunkak = Muszermunkak.objects.all()
    return render(
        request,
        'szabalyozok/riport_muszermunkak.html',
        {
            'title': 'Szabályozó munkák',
            'muszermunkak': muszermunkak,
        }
    )


@login_required(login_url='/login/')
def riport_szabtartozekok(request):
    szabtartozekok = Tartozekok.objects.all()
    return render(
        request,
        'szabalyozok/riport_szabtartozekok.html',
        {
            'title': 'Tartozékok',
            'szabtartozekok': szabtartozekok,
        }
    )


@login_required(login_url='/login/')
def riport_muszerek(request):
    muszerek = Muszerek.objects.all()
    return render(
        request,
        'szabalyozok/riport_muszerek.html',
        {
            'title': 'Muszerek',
            'muszerek': muszerek,
        }
    )


@login_required(login_url='/login/')
def riport_szabalyozok(request):
    szabalyozok = Szabalyozok.objects.all()
    return render(
        request,
        'szabalyozok/riport_szabalyozok.html',
        {
            'title': 'Szabalyozok',
            'szabalyozok': szabalyozok,
        }
    )

@login_required(login_url='/login/')
def riport_diagnosztika(request):
    diagnosztikak = Diagnosztika.objects.all()
    return render(
        request,
        'szabalyozok/riport_diagnosztikak.html',
        {
            'title': 'Diagnosztikák',
            'diagnosztikak': diagnosztikak,
        }
    )
