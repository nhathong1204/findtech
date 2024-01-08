from account.models import KYC, Account

def default(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            kyc = None
        account = Account.objects.get(user=request.user)
    else:
        account = None
        kyc = None
    return {
        'kyc': kyc,
        'account': account,
    }