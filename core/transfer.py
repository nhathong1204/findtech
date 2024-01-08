from django.shortcuts import render, redirect
from account.models import Account, KYC
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from core.models import Transaction
import time
from decimal import Decimal

@login_required
def search_user_account_number(request):
    # need to create kyc account
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You need to submit your kyc')
        return redirect('account:kyc-reg')
    ################################
    accounts = Account.objects.filter(account_status='active').exclude(user=request.user)
    # accounts = Account.objects.all()
    
    query = request.POST.get('account_number')
    if query:
        accounts = accounts.filter(
            Q(account_number=query) | Q(account_id=query)
        ).distinct()
    context = {
        'accounts': accounts
    }
    return render(request, 'transfer/search-user-by-account-number.html', context)

def AmountTransfer(request, account_number):
    # need to create kyc account
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You need to submit your kyc')
        return redirect('account:kyc-reg')
    ################################
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        messages.warning(request, 'Account does not exist')
        return redirect('core:search-account')
    
    context = {
        'account': account
    }
    return render(request, 'transfer/amount-transfer.html', context)
    
def AmountTransferProcess(request, account_number):
    # need to create kyc account
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You need to submit your kyc')
        return redirect('account:kyc-reg')
    ################################
    
    account = Account.objects.get(account_number=account_number) # get the account that the money could be sent to
    sender = request.user # the person that is logged in
    receiver = account.user # get the account of the person that is going to receive the money
    
    sender_account = request.user.account # get the currently logged in users account that could send the money
    receiver_account = account # get the person account that could receiver the money
    
    if request.method == "POST":
        amount = request.POST.get('amount-send')
        description = request.POST.get('description')
        
        if sender_account.account_balance >= Decimal(amount):
            new_transaction = Transaction.objects.create(
                user= request.user,
                amount=amount,
                description=description,
                receiver=receiver,
                sender=sender,
                sender_account=sender_account,
                receiver_account=receiver_account,
                status="processing",
                transaction_type="transfer",
            )
            new_transaction.save()
            transaction_id = new_transaction.transaction_id
            return redirect('core:transfer-confirmation', account.account_number, transaction_id)
        else:
            messages.warning(request, "Insufficient Fund.")
            return redirect('core:amount-transfer', account.account_number)
    else:
        messages.warning(request, "Error Occured, Try again later.")
        return redirect('account:dashboard')
            
def TransferConfirmation(request, account_number, transaction_id):
    # need to create kyc account
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You need to submit your kyc')
        return redirect('account:kyc-reg')
    ################################
    
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.exclude(status='completed').get(transaction_id=transaction_id)
    except:
        messages.warning(request, "Transaction does not exist")
        return redirect('account:dashboard')
    context = {
        'account': account,
        'transaction': transaction
    }
    return render(request, 'transfer/transfer-confirmation.html', context)

def TransferProcess(request, account_number, transaction_id):
    # need to create kyc account
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You need to submit your kyc')
        return redirect('account:kyc-reg')
    ################################
    
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    
    sender = request.user # the person that is logged in
    receiver = account.user # get the account of the person that is going to receive the money
    
    sender_account = request.user.account # get the currently logged in users account that could send the money
    receiver_account = account # get the person account that could receiver the money
    completed = False
    if request.method == 'POST':
        pin_number = request.POST.get('pin-number')
        if pin_number == sender_account.pin_number:
            transaction.status = 'completed'
            transaction.save()
            
            # remove the amount that I am sending from my account balance and update my account
            sender_account.account_balance -= transaction.amount
            sender_account.save()
            
            # add the amount that was removed from my account to the person that i am sending the money
            account.account_balance += transaction.amount
            account.save()
            
            messages.success(request, 'Transaction Successfully')
            time.sleep(3)
            return redirect('core:transfer-completed', account.account_number, transaction.transaction_id)
        else:
            messages.warning(request, 'Incorrect Pin')
            return redirect('core:transfer-confirmation', account.account_number, transaction.transaction_id)
    else:
        messages.warning(request, "Error Occured, Try again later.")
        return redirect('account:dashboard')
    
def TransferCompleted(request, account_number, transaction_id):
    # need to create kyc account
    try:
        kyc = KYC.objects.get(user=request.user)
    except:
        messages.warning(request, 'You need to submit your kyc')
        return redirect('account:kyc-reg')
    ################################
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, "Transfer does not exist")
        return redirect('account:dashboard')
    context = {
        'account': account,
        'transaction': transaction
    }
    return render(request, 'transfer/transfer-completed.html', context)