$(document).ready(function() {
    $(document).on('click','.transaction-detail',function(){
        let transaction_id = $(this).data('transaction-value')
        console.log('transaction_id',transaction_id)
        $('#transactionsMod').modal('show')

        $.ajax({
            url: '/ajax-transaction-detail',
            data: {
                'transaction_id': transaction_id,
            },
            dataType: 'json',
            success: function(res) {
                console.log('res',res)
                if(res.success == true && res.transaction_detail) {
                    $('#mainContent').html('')
                    $('#mainContent').html(res.transaction_detail)
                }
            }
        })
    })
    
    $(document).on('click','.ccard-detail',function(){
        let card_id = $(this).data('card-id')
        console.log('card_id',card_id)
        $('#cardPopup').modal('show')

        $.ajax({
            url: '/ajax-card-detail',
            data: {
                'card_id': card_id,
            },
            dataType: 'json',
            success: function(res) {
                console.log('res',res)
                if(res.success == true) {
                    $('#cardContent').html('')
                    $('#cardContent').html(res.card_detail)
                }
            }
        })
    })

    /****** Deposit Start *******/
    $(document).on('click','#nextDeposit, #depositAmountRedirect',function(){
        let card_id = $('input.chkboxDeposit:checked').attr('id')
        window.location.href = "/deposit-process/"+card_id+"/";
    })

    $(document).on('click','#submitDepositForm',function(){
        $('#submitFrmDeposit').trigger('click');
    })

    $(document).on('click','#submitDepositFinal',function(){
        deposit_amount = $(this).data('amount-value')
        card_id = $(this).data('credit-card-id')
        $.ajax({
            url: '/deposit-completed',
            data: {
                'card_id': card_id,
                'deposit_amount': deposit_amount,
            },
            dataType: 'json',
            success: function(res) {
                console.log('res',res)
                if(res.success == true) {
                    $('#congratulationsDeposit').modal('show');
                    // setTimeout(function() {
                    //     window.location.href = "/account/dashboard/";
                    // },2000)
                } else {
                    window.location.href = "/deposit-list-payments/";
                }
            }
        })
    })
    /****** Deposit End *******/
    
    /****** Withdraw Start *******/
    $(document).on('click','#nextWithDraw',function(){
        let card_id = $('input.chkboxWithdraw:checked').attr('id')
        window.location.href = "/withdraw-process/"+card_id+"/";
    })

    $(document).on('click','#submitWithDrawFinal',function(){
        withdraw_amount = $(this).data('amount-value')
        card_id = $(this).data('credit-card-id')
        $.ajax({
            url: '/withdraw-completed',
            data: {
                'card_id': card_id,
                'withdraw_amount': withdraw_amount,
            },
            dataType: 'json',
            success: function(res) {
                console.log('res',res)
                if(res.success == true) {
                    $('#congratulationsWithDraw').modal('show');
                    // setTimeout(function() {
                    //     window.location.href = "/account/dashboard/";
                    // },2000)
                } else {
                    window.location.href = "/withdraw-list-payments/";
                }
            }
        })
    })
    /****** Withdraw End *******/
})


