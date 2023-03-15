"""Interface for health_app"""
# imports
import pandas as pd
import pickle
import logging

with open("data/reg_model_2.pkl", "rb") as f:
    reg = pickle.load(f)


# input vars
genetic = float(input('Vul de genetische leeftijd in: '))
length = float(input('Vul de lengte in centimeters in: ')) 
mass = float(input ("Vul het lichaamsgewicht in hele kilo's in: "))
alcohol = float(input("Vul het aantal glazen alcohol per dag in: "))
sugar = float(input("Vul het aantal suikerklontjes per dag in: "))
smoking = float(input("Vul het aantal sigaretten per dag in: "))
exercise = float(input("Vul het aantal uren beweging per dag in: "))

    


#calculate bmi, lifespan and premie
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')



# to not have the error appear in the user interface: ```

data = {'genetic': genetic, 'length':[length],'mass': [mass], 
                                 'alcohol': [alcohol], 'sugar': [sugar], 
                                 'smoking': [smoking], 'exercise': [exercise], 'BMI': [bmi]}


df = pd.DataFrame.from_dict(data)
 
# lifespan_predict = reg.predict([[genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]])
lifespan_predict = reg.predict(df)

df['predict']=lifespan_predict

premie_factor = genetic/lifespan_predict

premie_korting = (1-premie_factor)*100


#print the results
print()
print(f'De levensverwachting is: {lifespan_predict}')
print()
print(f'De bmi is: {bmi}')
print()
print(f'De premiekorting is: {premie_korting} %')

