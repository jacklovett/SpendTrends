from django.db import models
from enum import auto
from _datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import default
from wallets.models import Wallet

activeWallet = Wallet.objects.filter(isActive=True).first()
  
# Create your models here.  
class Category(models.Model): 
    name = models.CharField(max_length = 50)
    isIncome = models.BooleanField(default=False, verbose_name="Income") 
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created Date")
    modifiedDate = models.DateTimeField(auto_now_add=True, verbose_name="Modified Date")
    
    def __str__(self): 
        return self.name 
     
class Transaction(models.Model): 
    description = models.TextField(null=True, blank=True)  
    walletId = models.ForeignKey(Wallet, default=activeWallet, on_delete=models.CASCADE, verbose_name="Wallet")
    categoryId = models.ForeignKey(Category, default=0, on_delete=models.CASCADE, verbose_name="Category")
    amount = models.DecimalField(decimal_places=2, max_digits=13, default=0.00)
    transactionDate = models.DateTimeField(default=timezone.now, verbose_name="Transaction Date")
    comments = models.TextField(null=True, blank=True)
    isPending = models.BooleanField(default=False, verbose_name="Pending Transaction")
    isRecurring = models.BooleanField(default=False, verbose_name="Recurring Transaction")
    isIncome = models.BooleanField(default=False, verbose_name="Income")
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created Date")
    modifiedDate = models.DateTimeField(auto_now_add=True, verbose_name="Modified Date")
        
    def __str__(self): 
        return self.description
          
    def get_absolute_url(self): 
        return reverse("transactions:detail", kwargs={"id": self.id}) 
 
     
    

    
    