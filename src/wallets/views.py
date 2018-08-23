from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import models
from . import forms
from django.core.mail.backends import console
from django.template.context_processors import request

# Create your views here. 
def wallets_list(request):
    wallets = models.Wallet.objects.all().order_by('-isActive') 
    context = {
        "wallets_list": wallets,
        "title":"Wallets" 
        }        
    return render(request, "wallets.html", context)  
  
def wallet_detail(request, id): 
    wallet = get_object_or_404(models.Wallet, id=id)
    context = {
        "wallet": wallet,
        "title":"Wallet"
        }
    return render(request, "wallet.detail.html", context)

def wallet_create(request):
    form = forms.WalletForm(request.POST or None)
    if form.is_valid():
        form = setCurrencyBalance(form)
        form.save()
        return HttpResponseRedirect('/wallets/')
    context = {
        "form": form, 
        "title": "Add New Wallet" 
        }
    return render(request, "wallet.form.html", context)

def setCurrencyBalance(form):
    form.instance.currentBalance = form.instance.initialBalance
    return form

def wallet_edit(request, id=None):
    wallet = get_object_or_404(models.Wallet, id=id)
    form = forms.WalletForm(request.POST or None, instance=wallet)
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect(wallet.get_absolute_url())        
    context = {
        "wallet": wallet,
        "title":"Edit Wallet",  
        "form": form
        }
    return render(request, "wallet.form.html", context) 

def wallet_delete(request, id=None):
    wallet = get_object_or_404(models.Wallet, id=id)
    wallet.delete()
    return HttpResponseRedirect('/wallets/') 