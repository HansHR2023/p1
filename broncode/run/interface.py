#!/usr/bin/env python


"""Interface for health_app"""
# imports
import pandas as pd
import pickle
import sys
import logging

with open("../build/regr_model.pkl", "rb") as f:
    reg = pickle.load(f)

# explanation
print()
print('Welkom bij de lifespan calculator! \n',
'- de calculator berekent de levensverwachting \n',
'- voer voor elk kenmerk een heel getal in binnen de gegeven range \n',
'- na 3 foutieve invoerpogingen stopt het programma')
print()

# hide error messages after 3 wrong inputs
sys.tracebacklimit = 0

# input sanitation
def inputDigit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)

        if inputStr.isdigit():
            inputNum = float(inputStr)

            if inputNum in acceptableRange:
                return inputNum

        i += 1
        if i == 3:
            raise Exception('driemaal een onjuiste invoer. Het programma is gestopt, maar kan opnieuw worden opgestart.')

# input vars
# genetic = float(input('Vul de genetische leeftijd in: '))
# length = float(input('Vul de lengte in centimeters in: ')) 
# mass = float(input ("Vul het lichaamsgewicht in hele kilo's in: "))
# exercise = float(input("Vul het aantal uren beweging per dag in: "))
# smoking = float(input("Vul het aantal sigaretten per dag in: "))
# alcohol = float(input("Vul het aantal glazen alcohol per dag in: "))
# sugar = float(input("Vul het aantal suikerklontjes per dag in: "))

acceptableRange_genetic = range(50,121)
acceptableRange_length = range(140,221)
acceptableRange_mass = range(40,171)
acceptableRange_alcohol = range(0,21)
acceptableRange_sugar = range(0,21)
acceptableRange_smoking = range(0,41)
acceptableRange_exercise = range(0,9)

genetic = int(inputDigit("De genetische leeftijd in jaren: [50 - 120]: ", acceptableRange_genetic))
length = int(inputDigit("De lengte in centimeters  [140 - 220]: ", acceptableRange_length))
mass = int(inputDigit("Het gewicht in in kg [40 - 170]: ", acceptableRange_mass))
alcohol = int(inputDigit("Het aantal glazen alcohol per dag [0 - 20]: ", acceptableRange_alcohol))
sugar = int(inputDigit("Het aantal suikerklontjes per dag [0 - 20]: ", acceptableRange_sugar))
smoking = int(inputDigit("Het aantal sigaretten per dag [0 - 40]: ", acceptableRange_smoking))
exercise = int(inputDigit("Het aantal uren beweging per dag [0 - 8]: ", acceptableRange_exercise))

#calculate bmi, lifespan and premie
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')



# to not have the error appear in the user interface: ```

data = {'genetic': genetic, 'length':[length],'mass': [mass], 'exercise': [exercise],
                                'smoking': [smoking], 'alcohol': [alcohol], 'sugar': [sugar], 
                                  'bmi': [bmi]}


df = pd.DataFrame.from_dict(data)
 
# lifespan_predict = reg.predict([[genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]])
lifespan_predict = reg.predict(df)

df['predict']=lifespan_predict

premie_factor = genetic/lifespan_predict

premie_korting = (1-premie_factor)*100


#print the results
print()
print(f'De levensverwachting is: {round(lifespan_predict[0], 2)}')
print()

print(f'De bmi is: {bmi}')
print()
if bmi < 18:
    print('De bmi classificatie is: ondergewicht')
elif bmi >= 18 and bmi < 25:
    print('De bmi classificatie is: normaal')
else:
    print('De bmi classificatie is: overgewicht')


print()
if premie_korting > 0:
    print(f'De premiekorting is: {round(premie_korting[0], 2)} %')
else:
    print(f'De premieverhoging is: {round(abs(premie_korting[0]), 2)} %')
print()
print()

