from datetime import datetime
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib import admin
import django.contrib.auth.views
import szabalyozok.forms
import szabalyozok.views
import debug_toolbar

urlpatterns = [
    # Examples:
    url(r'^$', szabalyozok.views.home, name='home'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'szabalyozok/login.html',
            'authentication_form': szabalyozok.forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Log in',
                    'year': datetime.now().year,
                }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # szabalyozó URL
    url(r'^szabalyozok/$', szabalyozok.views.szabalyozok, name='szabalyozok'),
    url(r'^szabalyozok/(?P<pk>[0-9]+)/show/$', szabalyozok.views.szabalyozo_show, name='szabalyozo_show'),
    url(r'^szabalyozok/(?P<pk>[0-9]+)/edit/$', szabalyozok.views.szabalyozo_edit, name='szabalyozo_edit'),
    url(r'^szabalyozok/(?P<pk>[0-9]+)/szabtartshow/$', szabalyozok.views.szabtart_show, name='szabtart_show'),
    url(r'^szabalyozok/(?P<pk>[0-9]+)/tartozekbeki/$', szabalyozok.views.tartozek_beki, name='tartozek_beki'),
    url(r'^szabalyozok/(?P<pk>[0-9]+)/szabterkep/$', szabalyozok.views.szabterkep, name='szabterkep'),
    url(r'^szabalyozok/(?P<pk>[0-9]+)/muszerbeki/$', szabalyozok.views.muszer_beki, name='muszer_beki'),
    url(r'^szabalyozok/(?P<pk>[0-9]+)/diagnosztika/$', szabalyozok.views.diagnosztika, name='diagnosztika'),
    url(r'^diagnosztika/(?P<pk>[0-9]+)/tortenet/$', szabalyozok.views.diagnosztika_tortenet, name='diagnosztika_tortenet'),
    url(r'^diagnosztika/(?P<pk>[0-9]+)/new/$', szabalyozok.views.diagnosztika_new, name='diagnosztika_new'),
    url(r'^szabalyozok/terkep/$', szabalyozok.views.terkep, name='terkep'),

    # tartozék URL
    url(r'^tartozek/(?P<pk>[0-9]+)/new/$', szabalyozok.views.tartozek_new, name='tartozek_new'),
    url(r'^tartozek/(?P<pk>[0-9]+)/tartozekki/$', szabalyozok.views.tartozek_ki, name='tartozek_ki'),
    url(r'^tartozek/(?P<pk>[0-9]+)/tartozektortenet/$', szabalyozok.views.tartozek_tortenet, name='tartozek_tortenet'),
    url(r'^tartozek/(?P<pk>[0-9]+)/(?P<spk>[0-9]+)/edit/$', szabalyozok.views.tartozek_edit, name='tartozek_edit'),

    # muszer URL
    url(r'^muszerek/(?P<pk>[0-9]+)/muszerki/$', szabalyozok.views.muszer_ki, name='muszer_ki'),
    url(r'^muszerek/(?P<pk>[0-9]+)/muszertortenet/$', szabalyozok.views.muszer_tortenet, name='muszer_tortenet'),
    url(r'^muszerek/(?P<pk>[0-9]+)/(?P<spk>[0-9]+)/muszerbe/$', szabalyozok.views.muszer_be, name='muszer_be'),
    url(r'^muszerek/manometernew/$', szabalyozok.views.manometernew, name='manometernew'),
    url(r'^manometer/(?P<pk>[0-9]+)/edit/$', szabalyozok.views.manometer_edit, name='manometer_edit'),

    # szabályozó munka URL
    url(r'^szabmunkak/(?P<pk>[0-9]+)/new/$', szabalyozok.views.szabmunka_new, name='szabmunka_new'),
    url(r'^szabmunkak/(?P<pk>[0-9]+)/show/$', szabalyozok.views.szabmunka_show, name='szabmunka_show'),
    url(r'^szabmunkak/(?P<pk>[0-9]+)/(?P<spk>[0-9]+)/edit/$', szabalyozok.views.szabmunka_edit, name='szabmunka_edit'),

    # műszer munka URL
    url(r'^muszermunkak/(?P<pk>[0-9]+)/(?P<spk>[0-9]+)/new/$', szabalyozok.views.muszermunka_new, name='muszermunka_new'),
    url(r'^muszermunkak/(?P<pk>[0-9]+)/(?P<spk>[0-9]+)/show/$', szabalyozok.views.muszermunka_show, name='muszermunka_show'),
    url(r'^muszermunkak/(?P<pk>[0-9]+)/(?P<mpk>[0-9]+)/(?P<spk>[0-9]+)/edit/$', szabalyozok.views.muszermunka_edit, name='muszermunka_edit'),

    # doc URL
    url(r'^doc/(?P<tip>[a-z]+)/(?P<eszid>[0-9]+)/(?P<spk>[0-9]+)/doclist/$', szabalyozok.views.doc_list, name='doc_list'),
    url(r'^doc/(?P<tip>[a-z]+)/(?P<eszid>[0-9]+)/(?P<spk>[0-9]+)/docnew/$', szabalyozok.views.doc_new, name='doc_new'),
    url(r'^doc/(?P<tip>[a-z]+)/(?P<pk>[0-9]+)/(?P<eszid>[0-9]+)/(?P<spk>[0-9]+)/docdel/$', szabalyozok.views.doc_del, name='doc_del'),

    # kép URL
    url(r'^kep/(?P<spk>[0-9]+)/keplist/$', szabalyozok.views.kep_list, name='kep_list'),
    url(r'^kep/(?P<spk>[0-9]+)/kepnew/$', szabalyozok.views.kep_new, name='kep_new'),
    url(r'^kep/(?P<pk>[0-9]+)/(?P<spk>[0-9]+)/kepdel/$', szabalyozok.views.kep_del, name='kep_del'),

    # riportok URL
    url(r'^riportok/szabmunkak/$', szabalyozok.views.riport_szabmunkak, name='riport_szabmunkak'),
    url(r'^riportok/muszermunkak/$', szabalyozok.views.riport_muszermunkak, name='riport_muszermunkak'),
    url(r'^riportok/szabtartozekok/$', szabalyozok.views.riport_szabtartozekok, name='riport_szabtartozekok'),
    url(r'^riportok/muszerek/$', szabalyozok.views.riport_muszerek, name='riport_muszerek'),
    url(r'^riportok/szabalyozok/$', szabalyozok.views.riport_szabalyozok, name='riport_szabalyozok'),
    url(r'^riportok/diagnosztikak/$', szabalyozok.views.riport_diagnosztika, name='riport_diagnosztika'),
    url(r'^riportok/riport_dokumentumfilter/$', szabalyozok.views.riport_dokumentumfilter, name='riport_dokumentumfilter'),

    # Riportok dokumnetum listája
    url(r'^riport/(?P<tip>[a-z]+)/(?P<eszid>[0-9]+)/simple_doc_list/$', szabalyozok.views.simple_doc_list, name='simple_doc_list'),

    # Apik
    # url(r'^api/(?P<pk>[0-9]+)/get_tartozekgyarto/$', szabalyozok.views.get_tartozekgyarto, name='get_tartozekgyarto'),
    url(r'^api/(?P<fpk>[0-9]+)/(?P<gpk>[0-9]+)/get_tartozektipus/$', szabalyozok.views.get_tartozektipus, name='get_tartozektipus'),

    # Új riport apik
    url(r'^riportok/riport_szabalyozok_api/$', szabalyozok.views.riport_szabalyozok_api, name='riport_szabalyozok_api'),
    url(r'^riportok/riport_szabtartozekok_api/$', szabalyozok.views.riport_szabtartozekok_api, name='riport_szabtartozekok_api'),
    url(r'^riportok/riport_muszerek_api/$', szabalyozok.views.riport_muszerek_api, name='riport_muszerek_api'),
    url(r'^riportok/riport_diagnosztika_api/$', szabalyozok.views.riport_diagnosztika_api, name='riport_diagnosztika_api'),
    url(r'^riportok/riport_szabmunkak_api/$', szabalyozok.views.riport_szabmunkak_api, name='riport_szabmunkak_api'),
    url(r'^riportok/riport_muszermunkak_api/$', szabalyozok.views.riport_muszermunkak_api, name='riport_muszermunkak_api'),

    url(r'^password/$', szabalyozok.views.change_password, name='change_password'),
]

# admin.autodiscover()


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]