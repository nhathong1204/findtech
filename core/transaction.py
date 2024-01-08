from django.shortcuts import render, redirect
from core.models import Transaction
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def transaction_list(request):
    sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type='transfer').order_by('-id')
    receiver_transaction = Transaction.objects.filter(receiver=request.user, transaction_type='transfer').order_by('-id')

    request_sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type='request').order_by('-id')
    request_receiver_transaction = Transaction.objects.filter(receiver=request.user, transaction_type='request').order_by('-id')
    context = {
        'sender_transaction': sender_transaction,
        'receiver_transaction': receiver_transaction,
        
        'request_sender_transaction': request_sender_transaction,
        'request_receiver_transaction': request_receiver_transaction,
    }
    return render(request, 'transaction/transaction-list.html', context)

@login_required
def ajax_transaction_detail(request):
    transaction_id = request.GET.get('transaction_id')
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    transaction_detail = render_to_string('transaction/transaction-detail.html', {'transaction': transaction})
        
    return JsonResponse(
        {
            'success': True,
            'transaction_detail': transaction_detail,
        }
    )