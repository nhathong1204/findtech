from django.db import models
from userauths.models import User
from account.models import Account
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('transfer', 'Transfer'),
        ('received', 'Received'),
        ('withdraw', 'Withdraw'),
        ('refund', 'Refund'),
        ('request', 'Payment Request'),
        ('none', 'none'),
    )
    TRANSACTION_STATUS = (
        ('failed', 'Failed'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('request_sent', 'Request Sent'),
        ('request_settled', 'Request Settled'),
        ('request_processing', 'Request Processing'),
    )
    transaction_id = ShortUUIDField(unique=True, length=15, max_length=20, prefix="TRN")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="transaction_user")
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    description = models.CharField(max_length=1000, null=True, blank=True)
    
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="receiver_user")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender_user")
    
    receiver_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="receiver_account")
    sender_account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="sender_account")
    
    status = models.CharField(choices=TRANSACTION_STATUS, max_length=100, default="none")
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=100, default="none")
    
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self) -> str:
        try:
            return f"{self.user}"
        except:
            return f"Transaction"
        
    def status_verbose(self):
        return dict(Transaction.TRANSACTION_STATUS)[self.status]
        
    def transaction_type_verbose(self):
        return dict(Transaction.TRANSACTION_TYPE)[self.transaction_type]
    
    
class CreditCard(models.Model):
    CARD_TYPE  = (
        ('master', 'Master'),
        ('visa', 'Visa'),
        ('verve', 'Verve'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_id = ShortUUIDField(unique=True, length=14, max_length=20, prefix="CARD", alphabet="1234567890")
    
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvv = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    card_type = models.CharField(choices=CARD_TYPE, max_length=20, default="master")
    card_status = models.BooleanField(default=True)
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}"
    
    def card_type_verbose(self):
        return dict(CreditCard.CARD_TYPE)[self.card_type]
    