from django.urls import path
from . import views, transfer, transaction, payment_request, credit_card, deposit_money, withdraw_money

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    # transfers
    path('search-account/', transfer.search_user_account_number, name='search-account'),
    path('amount-transfer/<account_number>/', transfer.AmountTransfer, name='amount-transfer'),
    path('amount-transfer-process/<account_number>/', transfer.AmountTransferProcess, name='amount-transfer-process'),
    path('transfer-confirmation/<account_number>/<transaction_id>/', transfer.TransferConfirmation, name='transfer-confirmation'),
    path('transfer-process/<account_number>/<transaction_id>/', transfer.TransferProcess, name='transfer-process'),
    path('transfer-completed/<account_number>/<transaction_id>/', transfer.TransferCompleted, name='transfer-completed'),

    # transaction
    path('transactions/', transaction.transaction_list, name='transactions'),
    path('ajax-transaction-detail/', transaction.ajax_transaction_detail, name='ajax-transaction-detail'),
    
    # payment request
    path('request-search-account/', payment_request.SearchUserRequest, name='request-search-account'),
    path('amount-request/<account_number>/', payment_request.AmountRequest, name='amount-request'),
    path('amount-request-process/<account_number>/', payment_request.AmountRequestProcess, name='amount-request-process'),
    path('amount-request-confirmation/<account_number>/<transaction_id>/', payment_request.AmountRequestConfirmation, name='amount-request-confirmation'),
    path('amount-request-final-process/<account_number>/<transaction_id>/', payment_request.AmountRequestFinalProcess, name='amount-request-final-process'),
    path('amount-request-completed/<account_number>/<transaction_id>/', payment_request.AmountRequestCompleted, name='amount-request-completed'),
    
    # request settlement 
    path('settlement-confirmation/<account_number>/<transaction_id>/', payment_request.SettlementConfirmation, name='settlement-confirmation'),
    path('settlement-processing/<account_number>/<transaction_id>/', payment_request.SettlementProcessing, name='settlement-processing'),
    path('settlement-completed/<account_number>/<transaction_id>/', payment_request.SettlementCompleted, name='settlement-completed'),
    path('delete-request/<account_number>/<transaction_id>/', payment_request.DeletePaymentRequest, name='delete-request'),
    
    # credit card
    path('ajax-card-detail/', credit_card.ajax_card_detail, name='ajax-card-detail'),
    
    # deposit money
    path('deposit-list-payments/', deposit_money.DepositListPayments, name='deposit-list-payments'),
    path('deposit-process/<card_id>/', deposit_money.DepositProcess, name='deposit-process'),
    path('deposit-completed/', deposit_money.AjaxDepositCompleted, name='deposit-completed'),
    
    # withdraw money
    path('withdraw-list-payments/', withdraw_money.WithdrawListPayments, name='withdraw-list-payments'),
    path('withdraw-process/<card_id>/', withdraw_money.WithdrawProcess, name='withdraw-process'),
    path('withdraw-completed/', withdraw_money.AjaxWithDrawCompleted, name='withdraw-completed'),
]
