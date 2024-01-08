from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import CreditCard, Transaction
from account.models import Account
from django.http import JsonResponse
from django.template.loader import render_to_string
from decimal import Decimal 
import time

@login_required
def DepositListPayments(request):
    credits = CreditCard.objects.filter(card_status=True, user=request.user)
    context = {
        'credits': credits
    }
    return render(request, 'deposit_payment/list-payment-links.html', context)

@login_required
def DepositProcess(request, card_id):
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = request.user.account
    # transaction = Transaction.objects.exclude(status='completed').get(transaction_id=transaction_id)
    
    if request.method == 'POST':
        deposit_amount = request.POST.get('deposit-amount')
        context = {
            'deposit_amount': deposit_amount,
            'account': account,
            'credit_card': credit_card,
        }
        return render(request, 'deposit_payment/deposit-confirmation.html', context)
    context = {
        'account': account,
        'credit_card': credit_card,
    }
    return render(request, 'deposit_payment/deposit-process.html', context)

@login_required
def AjaxDepositCompleted(request):
    card_id = request.GET.get('card_id')
    deposit_amount = request.GET.get('deposit_amount')
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = request.user.account
    
    if credit_card.amount >= Decimal(deposit_amount):
        account.account_balance += Decimal(deposit_amount)
        account.save()
        
        credit_card.amount -= Decimal(deposit_amount)
        credit_card.save()
        messages.success(request, "Deposit successfully")
        return JsonResponse(
            {
                'success': True,
            }
        )
    else:
        messages.warning(request, "Insufficient funds")
        return JsonResponse(
            {
                'success': False,
            }
        )
