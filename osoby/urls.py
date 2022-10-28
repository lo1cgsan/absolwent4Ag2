from django.urls import path

from . import views

app_name = 'osoby'
urlpatterns = [
    path('', views.lista_absolwentow, name='lista'),
    path('about/', views.about, name='about'),
    path('loguj/', views.loguj_osobe, name='loguj-osobe'),
]
