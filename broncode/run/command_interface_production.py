#!/usr/bin/env python

"""Interface for health_app"""
# imports
# import pickle
# import logging
import sqlite3
import pandas as pd
import sys
import logging
import pandas as pd
import statsmodels as sm
import statsmodels.formula.api as smf
import sqlite3
from datetime import datetime



# with open("reg.pkl", "rb") as f:
#     reg = pickle.load(f)



# open connection to SQLite.db
dbName = "../../rest_server/medisch_centrum_randstad/db.sqlite3"

dbConnection = sqlite3.connect(dbName)

# query db and write to pd:
dfFromDB = pd.read_sql_query(f"SELECT * FROM {'coef'}", dbConnection)
# sql adds index, remove:
df = dfFromDB.drop('index', axis=1)
pd.set_option('display.max_columns', 10)
# print(df.head(12))


# gdpr check. are we allowed to save this persons current input numbers?
# name is not asked to make the data GDPR proof. 

print ()
gdpr_check = input('Please ask if the patient grants permission to save the input of the data reguarding their current habits in accordance with the GDPR. If permission is granted type: Yes : ').title()


if gdpr_check == 'Yes':
    print ('This sessions patients initial data will be saved')
    client_nr = input ('Enter the patient nr : ').title()
    
    
else:
    print ('No data will be saved this session')


#hide errors, scary for the user xD
sys.tracebacklimit = 0 

# input safeguarding


def inputDigit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    inputNum = None
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)
        logging.debug(inputStr)

        if inputStr.isdigit():
            inputNum = float(inputStr)

            if inputNum in acceptableRange:
                return inputNum

        i += 1
        if i == 3:
            raise Exception("Number of incorrect inputs has been exceded. Programe will quit. It can be started again.")

    return None

  
# create df_q to have the values for the input questions to be asked. 
data_questions = {'feature': ['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise'],
        'acc_min': [50,140,40,0,0,0,0],
        'acc_max': [121,221,171,21,21,41,9],
        'per':['age in years','in cm','in kg','consumption in glasses per day',
               'consumption in cubes per day','in sigarettes per day','in hours per day'] }

# Create DataFrame
df_q = pd.DataFrame(data_questions) 

# print (df_q)
# create the function to ask the question per 'feature'
def input_q(name):
    min,max, per = df_q.loc[df_q['feature'] == name, ['acc_min','acc_max', 'per']].values[0]
    return int(inputDigit(f"Please enter, {name} {per} in the range: {min}-{max-1} ", range(min,max)))
    
# # test lines. 
# genetic = 77
# length = 177
# mass = 77
# alcohol = 2
# sugar = 2
# smoking = 2
# exercise = 2
# divider = pow(length/100, 2) if length >0 else None
# bmi = round(mass/divider)
# logging.debug(f'bmi: {bmi}')

print()

genetic = input_q ('genetic')
length = input_q ('length')
mass = input_q ('mass')
alcohol = input_q ('alcohol')
sugar = input_q ('sugar')
smoking = input_q ('smoking')
exercise = input_q ('exercise')
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')

input_nr = 1

# initialize data of lists.
data = {'feature': ['genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise', 'bmi'],
        f'input_{input_nr}': [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]}
  
# Create DataFrame
df_input = pd.DataFrame(data)
print('This sessions data has been saved to an SQLite.db')


# multiply the rows of df and df_input for the relevant row. add the interceptor where the data crosses the y-axis. 
lifespan_predicted = int(sum(df_input['input_1'].multiply(df['coef']))+ df['intercept'][0])

print()
print(f'the predicted lifespan is: {lifespan_predicted}')
print ()

# create df to be saved and save it in SQL
# create date
date = datetime.now().strftime("%Y-%m-%d")

if gdpr_check == 'Yes':
    data_to_save = {'feature': ['client_nr','date','lifespan_predicted','genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise'],
        f'{client_nr}_{date}': [client_nr, date, lifespan_predicted, genetic, length, mass, alcohol, sugar, smoking, exercise]}

    df_to_SQL = pd.DataFrame(data_to_save)
    df_to_SQL.to_sql(f'{client_nr}_{date}', if_exists='replace', con=dbConnection)

# close SQL connection
dbConnection.close()

    # print (df_to_SQL)

# df_save_to_SQLlite = 
############## nog bouwen!!!!!!!!!!

# transpose df input for finish function
# df_input=df_input.transpose()

# print(df_input)
# df_input['predicted_lifespan']=[lifespan_predicted]

def finised ():
    end_programme = input('press any key to show all results and exit the programme.')
    print()
    print (df_input)
    return quit()





# 2nd round of questions
print()
round_2 = input('If you want to see what happens to predicted life expectancy if the patient changes their habits. Type Yes : ').title()
print()

if round_2 != 'Yes':
    finised() 
   


# ask the relevant changable questions again. 
mass = input_q ('mass')
alcohol = input_q ('alcohol')
sugar = input_q ('sugar')
smoking = input_q ('smoking')
exercise = input_q ('exercise')
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')


# use results to create new df column with original and ammended data. 
df_input['input_2'] = [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]


# multiply the rows of df and df_input for the relevant row. add the interceptor where the data crosses the y-axis. 
lifespan_predicted2 = int(sum(df_input['input_2'].multiply(df['coef']))+ df['intercept'][0])
#df_input['predicted_lifespan']=[lifespan_predicted,lifespan_predicted2]
print()
print(f'Your 1st predicted lifespan is:: {lifespan_predicted}')
print(f'Your 2nd predicted lifespan is: {lifespan_predicted2}')
print()

# 3rd round of questions
print()
round_3 = input('If you want to see what happens to predicted life expectancy if the patient changes their habits. Type Yes : ').title()
print()

if round_3 != 'Yes':
    finised()


# ask the relevant changable questions again. 
mass = input_q ('mass')
alcohol = input_q ('alcohol')
sugar = input_q ('sugar')
smoking = input_q ('smoking')
exercise = input_q ('exercise')
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')


# use results to create new df column with original and ammended data. 
df_input['input_3'] = [genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]

# multiply the rows of df and df_input for the relevant row. add the interceptor where the data crosses the y-axis. 
lifespan_predicted3 = int(sum(df_input['input_3'].multiply(df['coef']))+ df['intercept'][0])
# df_input['predicted_lifespan']=[lifespan_predicted,lifespan_predicted2,lifespan_predicted3]
print()
print(f'Your 1st predicted lifespan is:: {lifespan_predicted}')
print(f'Your 2nd predicted lifespan is: {lifespan_predicted2}')
print(f'Your 3nd predicted lifespan is: {lifespan_predicted3}')
print()

# end programme

finised()
