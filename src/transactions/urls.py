from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.transactions_list, name="list"),  
    url(r'^(?P<id>\d+)/$', views.transaction_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', views.transaction_edit, name="edit"),
    url(r'^create/$', views.transaction_create, name="create"),
    url(r'^(?P<id>\d+)/delete/$', views.transaction_delete, name="delete")
]  
