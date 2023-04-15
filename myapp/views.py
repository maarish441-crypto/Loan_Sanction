from django.shortcuts import render , HttpResponse
from ML.loan_sanc_predictor import predictI
import pandas as pd

# Create your views here.


def index(request):
    return render(request,"index.html")


def predict(request):
    if request.method == 'POST':
        gen = request.POST['Gender']
        marr = request.POST['Married']
        edu = request.POST['Education']
        se_em = request.POST['Self_Employed']
        app_inc = request.POST['ApplicantIncome']
        co_app_inc = request.POST['CoapplicantIncome']
        lo_amt = request.POST['LoanAmount']
        lo_amt_tm = request.POST['Loan_Amount_Term']
        cred_his = request.POST['Credit_History']
        prop_ar = request.POST['Property_Area']


        result = predictI(pd.DataFrame([[gen,marr,edu,se_em,app_inc,co_app_inc,lo_amt,lo_amt_tm,cred_his,prop_ar]]))
        context = {"Result":result}
        return render(request,"prediction.html",context=context)
    else:
        return HttpResponse("error")






