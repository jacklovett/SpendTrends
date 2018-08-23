from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.wallets_list, name="list"),
    url(r'^(?P<id>\d+)/$', views.wallet_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', views.wallet_edit, name="edit"),
    url(r'^create/$', views.wallet_create, name="create"),
    url(r'^(?P<id>\d+)/delete/$', views.wallet_delete, name="delete")     
] 