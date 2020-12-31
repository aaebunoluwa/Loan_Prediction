function approveLoan(){
    console.log("Approve loan button clicked");
    var total_income = document.getElementById('total_income');
    var monthly_loan_payment = document.getElementById('monthly_payment');
    var income_balance = document.getElementById('income_balance');
    var credit_history = getCreditHistory();
    var approval = document.getElementById('approval');
    var url = '/make_prediction';

    $.post(url, 
        {
            Credit_History : credit_history,
            Total_Income : parseFloat(total_income.value),	
            Monthly_Loan_Payment: parseFloat(monthly_loan_payment.value),	
            Monthly_Balance: parseFloat(income_balance.value)
        },
        function(data, status){
            console.log(data.model_prediction);
            if (parseInt(data.model_prediction) == 1){
                approval.innerHTML = '<h2>'+ 'Approved' + '</h2>'

            }
            else{
                approval.innerHTML = '<h2>'+ 'Rejected' + '</h2>'

            }
            console.log(status);

        }
        );
}


function getCreditHistory(){
    var credit_history = document.getElementsByName('credit_history');
    for (var i in credit_history){
        if (credit_history[i].checked){
            return parseFloat(i)
        }
    }
    return -1;
}