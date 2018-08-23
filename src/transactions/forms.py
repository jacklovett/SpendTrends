from django import forms
from . import models

class TransactionForm(forms.ModelForm): 
    class Meta:
        model = models.Transaction
        fields = [
            "description", 
            "walletId", 
            "categoryId",
            "amount", 
            "transactionDate",
            "isRecurring",
            "isIncome",
            "comments"              
            ]
    
    

