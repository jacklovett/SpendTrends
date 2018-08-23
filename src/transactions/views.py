from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from . import models
from . import forms 
from django.core.mail.backends import console
from django.template.context_processors import request
from wallets.models import Wallet as wallet
from django.forms.forms import Form

# Create your views here. 
# transactions views 
def transactions_list(request): 
    transactions = models.Transaction.objects.all().order_by("-createdDate")  
    activeWallet = wallet.objects.filter(isActive=True).first()
    context = {  
        "transactions_list": transactions, 
        "active_wallet": activeWallet,
        "title":"Transactions" 
        }  
    return render(request, "transactions.html", context)  
 
def transaction_detail(request, id): 
    transaction = get_object_or_404(models.Transaction, id=id)
    context = {
        "transaction": transaction,
        "title":"Transaction" 
        }
    return render(request, "transaction.detail.html", context)

def transaction_create(request):
    form = forms.TransactionForm(request.POST or None)
    if form.is_valid():
        saveTransaction(form)
        return HttpResponseRedirect('/transactions/')
    context = {
        "form": form, 
        "title": "Add New Transaction"
        }
    return render(request, "transaction.form.html", context)

def transaction_edit(request, id=None):
    transaction = get_object_or_404(models.Transaction, id=id)
    form = forms.TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        saveTransaction(form)
        return HttpResponseRedirect(transaction.get_absolute_url())        
    context = { 
        "transaction": transaction,
        "title":"Edit Transaction",
        "form": form
        }
    return render(request, "transaction.form.html", context)

def transaction_delete(request, id=None):
    transaction = get_object_or_404(models.Transaction, id=id)
    walletToUpdate = transaction.walletId
    transaction.delete()
    updateCurrentBalance(walletToUpdate)
    return HttpResponseRedirect('/transactions/')     

# form handler to control the change in the wallets current balance
def saveTransaction(form):
    form = isExpense(form)
    form.save() 
    updateCurrentBalance(form.instance.walletId)
    return 

def isExpense(form):
    if  form.instance.isIncome == False and form.instance.amount > 0:
        form.instance.amount = -1 * form.instance.amount    
    return form

def updateCurrentBalance(wallet):
    trans = models.Transaction.objects.filter(walletId = wallet)
    totalTransAmount = (sum(tran.amount for tran in trans))
    wallet.currentBalance = wallet.initialBalance + totalTransAmount
    wallet.save()  
    return
  
# category views
def categories_list(request): 
    categories = models.Category.objects.all()
    context = { 
        "categories_list": categories, 
        "title":"Categories"
        }
    return render(request, "transactions.html", context)
