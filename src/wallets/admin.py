from django.contrib import admin
from . import models

# Register your models here.
class WalletModelAdmin(admin.ModelAdmin):
    list_display = ["name", "initialBalance", "currentBalance", "currency", "isActive", "modifiedDate", "createdDate"]
    search_fields = ["name"]
    class Meta:
        model = models.Wallet
          
admin.site.register(models.Wallet, WalletModelAdmin)  