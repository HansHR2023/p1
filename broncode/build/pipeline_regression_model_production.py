#!/usr/bin/env python

# Goal: Output the model coefficients into the SQL database as table:'coef'
# Regression Model Winner: DF4 🥳 runner up DF5 🤯

from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn import linear_model 
from sklearn.model_selection import train_test_split
import math
import sqlite3
from os import system
import pickle

# runs the pipeline to ensure to run regression from the most up to date data.
# system('python broncode/build/pipeline_data_model_production.py') 

#import model data from pipeline, in this case SQLlite in same folder 
## saving the new df to SQL

dbName = "../../rest_server_new/medisch_centrum_randstad/db.sqlite3"
# tableName = "df4"

dbConnection = sqlite3.connect(dbName)

# query db and write to pd:
dfFromDB = pd.read_sql_query(f"SELECT * FROM {'df4'}", dbConnection)
# sql adds index, remove:
df = dfFromDB.drop('index', axis=1)
pd.set_option('display.max_columns', 10)
# print(df.head())



# #import model data from pipeline, in this case CSV in same folder 
# df = pd.read_csv('df4.csv',sep=',',skipinitialspace=True)
# df = df.drop('Unnamed: 0', axis=1)

#split the data in train and test sets with agreed 0.2 size and 42 as seed for the random state
train, test = train_test_split(df, test_size=0.2, random_state=42)
X = train.drop(columns=['lifespan'])
y = train.lifespan

#fit the model
regr = linear_model.LinearRegression()
regr.fit(X, y) 

#R-squared model score
score = regr.score(test.drop(columns=['lifespan']),test.lifespan)
rsquaredscore = score

#Root-Mean-Squared-Error (RMSE)
p_test = regr.predict(test.drop(columns=['lifespan']))
mse = mean_squared_error(test.lifespan, p_test)
rmse = (math.sqrt(mse))

#Regression Coefficients
coef = regr.coef_
intercept = regr.intercept_

#Store variables in SQL table
dfdrop = df.drop(columns=['lifespan'])
df_coef = pd.DataFrame({'feature':dfdrop.columns,'coef': coef,'intercept': intercept,'rsquared':score,'rmse':rmse})
df_coef.to_sql('coef', if_exists='replace', con=dbConnection)
print('Generated coef: succesfully written to SQL database')

# close SQL connection
dbConnection.close()

# save trained model to pickle
with open("regr_model.pkl", "wb") as f:
    pickle.dump(regr, f)

