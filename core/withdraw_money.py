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
def WithdrawListPayments(request):
    credits = CreditCard.objects.filter(card_status=True, user=request.user)
    context = {
        'credits': credits
    }
    return render(request, 'withdraw_payment/list-payment-links.html', context)

@login_required
def WithdrawProcess(request, card_id):
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = request.user.account
    # transaction = Transaction.objects.exclude(status='completed').get(transaction_id=transaction_id)
    
    if request.method == 'POST':
        withdraw_amount = request.POST.get('withdraw-amount')
        context = {
            'withdraw_amount': withdraw_amount,
            'account': account,
            'credit_card': credit_card,
        }
        return render(request, 'withdraw_payment/withdraw-confirmation.html', context)
    context = {
        'account': account,
        'credit_card': credit_card,
    }
    return render(request, 'withdraw_payment/withdraw-process.html', context)

# @login_required
def AjaxWithDrawCompleted(request):
    card_id = request.GET.get('card_id')
    withdraw_amount = request.GET.get('withdraw_amount')
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    account = request.user.account
    
    if credit_card.amount >= Decimal(withdraw_amount):
        account.account_balance -= Decimal(withdraw_amount)
        account.save()
        
        credit_card.amount += Decimal(withdraw_amount)
        credit_card.save()
        messages.success(request, "Withdraw successfully")
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
