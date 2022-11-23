from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import pickle
import os 
from django.conf import settings

#model = pickle.load(open('model.pkl', 'rb'))

# Create your views here.

pred_output = 0
pred_proba = 0

def home(request):
    return render(request, 'webapp/index.html')

def open_model(file_name):
    models_folder = settings.BASE_DIR / 'webapp/modelsfg'
    file_path = os.path.join(models_folder, os.path.basename(file_name))
    return file_path

def sendData(request):
    if request.method == 'POST':
        pclass = int(request.POST.get('pclass'))
        fare =  int(request.POST.get('fare'))
        sex = request.POST.get('sex')
        print(pclass, fare, sex)

        pathh = open_model('model.pkl')
        print("djkffhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", pathh)
        model = pickle.load(open(pathh, 'rb'))

        if pclass == 1:
		    # Remember pclass == 0 when pclass_2 and pclass_3 are both 0.
            pclass_2 = 0
            pclass_3 = 0

        elif pclass == 2:
            pclass_2 = 1
            pclass_3 = 0

        elif pclass == 3:
            pclass_2 = 0
            pclass_3 = 1

        if sex == 'Male':
            sex_male_int = 1
        else:
            sex_male_int = 0

        print(fare, pclass_2, pclass_3, sex_male_int)

        to_predict = [fare, pclass_2, pclass_3, sex_male_int]

        # make a prediction
        prediction = model.predict([to_predict])
        prediction_proba = model.predict_proba([to_predict])
        print("Pred Proba", prediction_proba)

        # extract the predicted value. 
        value = prediction[0]

        # if it predicts zero, then make output 'Death' else 'Survived'
        # also get the predicted probability 
        if value == 0:
            pred_output = 'Death'
            pred_proba = prediction_proba[0][0].round(2) * 100
        else:
            pred_output = 'Survival'
            pred_proba = prediction_proba[0][1].round(2) * 100

        print('pred_output:', pred_output)

        return JsonResponse({'status': 'Successful POST request!'})
        

# def show_result(request):
#     pred_output = request.session.get('pred_output')
#     pred_proba =  request.session.get('pred_proba')
#     context = { 
#             'pred_output': pred_output,
#             'pred_proba' : pred_proba
#     }
#     return render(request, 'webapp/show-result.html', context)

