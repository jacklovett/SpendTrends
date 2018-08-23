from django.db import models
from enum import auto
from _datetime import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import default

# Create your models here. 
class Wallet(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(null=True, blank=True)
    currency = models.CharField(max_length = 10) 
    initialBalance = models.DecimalField(decimal_places=2, max_digits=13, default=0.00, verbose_name="Initial Balance")
    currentBalance = models.DecimalField(decimal_places=2, max_digits=13, default=0.00, verbose_name="Current Balance")
    isActive = models.BooleanField(default=False, verbose_name="Active")
    createdDate = models.DateTimeField(auto_now_add=True, auto_now=False,  verbose_name="Created Date")
    modifiedDate = models.DateTimeField(auto_now_add=True, verbose_name="Modified Date") 
           
    def __str__(self):
        return self.name   
       
    def get_absolute_url(self):  
        return reverse("wallets:detail", kwargs={"id": self.id})    