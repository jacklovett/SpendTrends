from django.contrib import admin
from . import models

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "isIncome", "createdDate"]
    search_fields = ["name"]
    list_filter = ["isIncome"]
    class Meta:
        model = models.Category 
        
class TransactionModelAdmin(admin.ModelAdmin):
    list_filter = ["categoryId", "isIncome", "isRecurring", "transactionDate", "createdDate"]
    search_fields = ["description"]
    list_display = ["description",
        "categoryId",
        "amount", 
        "comments",
        "isIncome",
        "isRecurring",
        "transactionDate",
        "createdDate"
        ]      
    class Meta:
        model = models.Transaction    

admin.site.register(models.Category, CategoryModelAdmin)
admin.site.register(models.Transaction, TransactionModelAdmin)