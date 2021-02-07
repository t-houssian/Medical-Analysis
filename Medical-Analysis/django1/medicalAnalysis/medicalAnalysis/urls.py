from django.urls import path

from . import views

app_name = 'medicalAnalysis'
urlpatterns = [
    path('', views.data, name='medicalAnalysis')
]
