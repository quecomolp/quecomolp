from django.conf.urls import patterns, url

from appQueComo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^registro/$', views.registro, name='registronegocio'),
    url(r'^contacto/$', views.contacto, name='contactopersonas'),
)