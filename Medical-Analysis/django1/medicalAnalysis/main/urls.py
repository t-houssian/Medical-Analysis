from bokeh.server.django import autoload

from django.conf.urls import url
from django.apps import apps
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

import medicalAnalysis.pn_app as medicalAnalysis_app

pn_app_config = apps.get_app_config('bokeh.server.django')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/', views.special, name='special'),

    path('medicalAnalysis/', include('medicalAnalysis.urls')),
]

bokeh_apps = [
    autoload("medicalAnalysis", medicalAnalysis_app.app),
]

urlpatterns += staticfiles_urlpatterns()
