from django.shortcuts import HttpResponse, render
import numpy as np
import pandas as pd
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home")








def solution(request):
    loan_limit = float(request.POST.get('loan_limit'))
    gender = float(request.POST.get('Gender'))
    approv_in_adv = float(request.POST.get('approv_in_adv'))
    loan_type = float(request.POST.get('loan_type'))
    loan_purpose = float(request.POST.get('loan_purpose'))
    credit_worthiness = float(request.POST.get('Credit_Worthiness'))
    open_credit = float(request.POST.get('open_credit'))
    business_or_commercial = float(request.POST.get('business_or_commercial'))
    loan_amount = float(request.POST.get('loan_amount'))
    rate_of_interest = float(request.POST.get('rate_of_interest'))
    interest_rate_spread = float(request.POST.get('interest_rate_spread'))
    upfront_charges = float(request.POST.get('upfront_charges'))
    term = float(request.POST.get('term'))
    neg_ammortization = float(request.POST.get('neg_ammortization'))
    interest_only = float(request.POST.get('interest_only'))
    lump_sum_payment = float(request.POST.get('lump_sum_payment'))
    property_value = float(request.POST.get('property_value'))
    construction_type = float(request.POST.get('construction_type'))
    occupancy_type = float(request.POST.get('occupancy_type'))
    secured_by = float(request.POST.get('secured_by'))
    total_units = float(request.POST.get('total_units'))
    income = float(request.POST.get('income'))
    credit_type = float(request.POST.get('credit_type'))
    credit_score = float(request.POST.get('credit_score'))
    co_applicant_credit_type = float(request.POST.get('co_applicant_credit_type'))
    age = float(request.POST.get('age'))
    submission_of_application = float(request.POST.get('submission_of_application'))
    ltv = float(request.POST.get('ltv'))
    region = float(request.POST.get('region'))
    security_type = float(request.POST.get('security_type'))
    dtir1g = float(request.POST.get('dtir1g'))
    approv_in_adv = float(request.POST.get('approv_in_adv'))
    approv_in_adv = float(request.POST.get('approv_in_adv'))


    list = [[loan_limit , gender , approv_in_adv , loan_type , loan_purpose , credit_worthiness , open_credit ,  business_or_commercial , loan_amount , rate_of_interest , interest_rate_spread , upfront_charges , term , neg_ammortization , interest_only , lump_sum_payment , property_value , construction_type , occupancy_type , secured_by , total_units , income , credit_type , credit_score , co_applicant_credit_type , age , submission_of_application , ltv , region , security_type , dtir1g]]

    # arr = ['loan_limit' , 'gender' , 'approv_in_adv' , 'loan_type' , 'loan_purpose' , 'credit_worthiness' , 'open_credit' ,  'business_or_commercial' , 'loan_amount' , 'rate_of_interest' , 'interest_rate_spread' , 'upfront_charges' , 'term' , 'neg_ammortization' , 'interest_only' , 'lump_sum_payment' , 'property_value' , 'construction_type' , 'occupancy_type' , 'secured_by' , 'total_units' , 'income' , 'credit_type' , 'credit_score' , 'co_applicant_credit_type' , 'age' , 'submission_of_application' , 'ltv' , 'region' , 'security_type' , 'dtir1g']

    arr = arr = ['loan_limit' , 'Gender' , 'approv_in_adv' , 'loan_type' , 'loan_purpose' , 'Credit_Worthiness' , 'open_credit' ,  'business_or_commercial' , 'loan_amount' , 'rate_of_interest' , 'Interest_rate_spread' , 'Upfront_charges' , 'term' , 'Neg_ammortization' , 'interest_only' , 'lump_sum_payment' , 'property_value' , 'construction_type' , 'occupancy_type' , 'Secured_by' , 'total_units' , 'income' , 'credit_type' , 'Credit_Score' , 'co-applicant_credit_type' , 'age' , 'submission_of_application' , 'LTV' , 'Region' , 'Security_Type' , 'dtir1']

    import joblib
    import numpy as np
    import pandas as pd


    model = joblib.load('loan_status_predict')


    df = pd.DataFrame(list, columns = arr[:])

    status = model.predict(df)

    print(status)
    print(type(status))

    if status == 1:
        status_loan = 'You are eligible for loan.'

    else:
        status_loan = 'You are not eligible for loan'

    status = model.predict(df)

    # for i in list:
    #     print(i)
    # print(list)
    return render(request, 'solution.html',
                  {'status_loan': status_loan})
    # return HttpResponse("This is solution")