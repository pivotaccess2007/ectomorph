# vim: expandtab ts=2
from django.conf.urls import patterns, include, url
from django.contrib import admin
import rapidsmsrw1000.apps.thoureport.views as views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.smser', name='smser'),
    url(r'^sendsms$', 'views.sender', name='sender'),

    url(r'^responses$', 'views.responses', name='responses'),
    url(r'^modresp/(.+)$', 'views.resp_mod', name='resp_mod'),

    url(r'^messages$', 'views.messages', name='messages'),
    url(r'^reports(/\w+)?$', 'views.reports', name='reports'),
    url(r'^docs?$', 'views.docs', name='docs'),

    url(r'^admin/', include(admin.site.urls)),
)


# from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
import rapidsmsrw1000.apps.ubuzima.views as views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^reporter/(?P<pk>\d+)$', views.by_reporter),
    url(r'^patient/(?P<pk>\d+)$', views.by_patient),
    url(r'^national_id/(?P<national_id>\d+)$', views.by_national_id),
    url(r'^type/(?P<pk>\d+)$', views.by_type),
    url(r'^location/(?P<pk>\d+)$', views.by_location),
    url(r'^report/(?P<pk>\d+)$', views.view_report),

    url(r'^dash/pre$', views.preg_report),
    url(r'^dash/pcalendar$', views.pregnancy_calendar),
    url(r'^dash/pcalendar/data$', views.pregnancy_calendar_data),
    url(r'^dash/pnc$', views.pnc_report),
    url(r'^dash/anc$', views.anc_report),
    url(r'^dash/bir$', views.birth_report),
    url(r'^dash/de$', views.death_report),
    url(r'^dash/ris$', views.risk_report),
    url(r'^dash/red$', views.red_alert_report),
    url(r'^dash/chi$', views.child_report),
    url(r'^dash/chi/(?P<pk>\d+)$', views.child_details_report),
    url(r'^dash/admin$', views.admin_report),
    url(r'^newborn$', views.newborn_report),
    url(r'^ccm$', views.community_report),
    url(r'^ibibari$', views.ibibari),
    url(r'^reminders$', views.view_reminders),
    url(r'^deliverynots$', views.view_delivery_nots),
    url(r'^reminders/type/(?P<pk>\d+)$', views.remlog_by_type),
    url(r'^alerts$', views.view_alerts),
    url(r'^alerts/type/(?P<pk>\d+)$', views.alerts_by_type),
    url(r'^indicator/(?P<indic>\d+)/(?P<format>html|csv)$', views.view_indicator),
    url(r'^nutrition$', views.nutrition),
    url(r'^nutrition/data/$', views.nutrition_data),
    url(r'^nutrition/(?P<indic>\d+)/(?P<format>html|csv)$', views.view_nutrition),
    url(r'^charts$', views.view_nutrition_charts),
    url(r'^emergency$', views.emergency_room),

    url(r'^vaccination$',views.view_chihe),
    url(r'^vaccination/(?P<format>\w+)/(?P<dat>\w+)$',views.chihe_stats),
    
)
