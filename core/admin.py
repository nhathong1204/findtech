from django.contrib import admin
from core.models import Transaction, CreditCard

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_editable = ('amount', 'receiver', 'sender', 'transaction_type', 'status')
    list_display = ('transaction_id', 'user', 'amount', 'receiver', 'sender', 'transaction_type', 'status')
    

class CreditCardAdmin(admin.ModelAdmin):
    list_editable = ('amount', 'card_type')
    list_display = ('user', 'amount', 'card_type')
    
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
