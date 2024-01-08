from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import CreditCard
from account.models import Account
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def ajax_card_detail(request):
    card_id = request.GET.get('card_id')
    account = Account.objects.get(user=request.user)
    credit_card = CreditCard.objects.get(card_id=card_id, user=request.user)
    
    # context = {
    #     'account': account,
    #     'credit_card': credit_card
    # }
    # return render(request, 'credit_card/card-detail.html', context)
    card_detail = render_to_string('credit_card/card-detail.html', {'credit_card': credit_card})
        
    return JsonResponse(
        {
            'success': True,
            'card_detail': card_detail,
        }
    )
    
