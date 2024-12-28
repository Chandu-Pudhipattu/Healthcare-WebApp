from django.shortcuts import render
from django.http import HttpResponse
import joblib

model = joblib.load('static/heart_disease_prediction_model')
model_xgb = joblib.load('static/xgb_classifier')
model_reg = joblib.load('static/random_forest_regressor')

# Create your views here.

def home(request):
    return render(request,'home.html')

def heart(request):
    output = None
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cp = int(request.POST.get('cp'))
        trestbps = int(request.POST.get('trestbps'))
        chol = int(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        restecg = int(request.POST.get('restecg'))
        thalach = int(request.POST.get('thalach', 0) or 0)
        exang = int(request.POST.get('exang'))
        oldpeak = float(request.POST.get('oldpeak'))
        slope = int(request.POST.get('slope'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thal'))

        pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,thal]])

        # Check prediction and set appropriate message
        if pred[0] == 1:
            output = "You're Heart is at Risk, Please Consult Doctor Immediately"
        else:
            output = "You're Healthy and Strong!"

    return render(request, 'heart.html', {'output': output})

def parkinsons(request):
    output = None
    if request.method == 'POST':
        name = int(request.POST.get('name'))
        MDVP_Fo = float(request.POST.get('MDVP_Fo'))
        MDVP_Fhi = float(request.POST.get('MDVP_Fhi'))
        MDVP_Flo = float(request.POST.get('MDVP_Flo'))
        MDVP_Jitter = float(request.POST.get('MDVP_Jitter'))
        MDVP_Jitter_Abs = float(request.POST.get('MDVP_Jitter_Abs'))
        MDVP_RAP = float(request.POST.get('MDVP_RAP'))
        MDVP_PPQ = float(request.POST.get('MDVP_PPQ'))
        Jitter_DDP = float(request.POST.get('Jitter_DDP'))
        MDVP_Shimmer = float(request.POST.get('thalach', 0) or 0)
        MDVP_Shimmer_dB = float(request.POST.get('MDVP_Shimmer_dB',0) or 0)
        Shimmer_APQ3 = float(request.POST.get('Shimmer_APQ3'))
        Shimmer_APQ5 = float(request.POST.get('Shimmer_APQ5'))
        MDVP_APQ = float(request.POST.get('MDVP_APQ'))
        Shimmer_DDA = float(request.POST.get('Shimmer_DDA'))
        NHR = float(request.POST.get('NHR'))
        HNR = float(request.POST.get('HNR'))
        PDE = float(request.POST.get('RPDE'))
        DFA = float(request.POST.get('DFA'))
        spread1 = float(request.POST.get('spread1'))
        spread2 = float(request.POST.get('spread2'))
        D2 = float(request.POST.get('D2'))
        PPE = float(request.POST.get('PPE'))

        # Prepare the input data for prediction (make sure the data format matches your model's input)
        features = [
                    name, MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, 
                    Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA,
                    NHR, HNR, PDE, DFA, spread1, spread2, D2, PPE
                ]
        
        # Perform the prediction
        prediction = model_xgb.predict([features])

        if prediction[0] == 1:
            output = "You're at Risk, Please Consult Doctor Immediately"
        else:
            output = "You're Healthy and Strong!"

        # Display predicted result
    return render(request, 'parkinsons.html', {'output': output})   

def insurance(request):
    output = None
    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        #print(age,sex,bmi,children,smoker,region)

        pred = round(model_reg.predict([[age,sex,bmi,children,smoker,region]])[0])

        output = {
            "output" : pred
        }

    return render(request,'insurance.html',{'output':output})


