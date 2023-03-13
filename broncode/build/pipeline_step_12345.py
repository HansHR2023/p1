# Imports
import logging
import pandas as pd
# import requests
import sqlite3
from sklearn import linear_model
from sklearn.model_selection import train_test_split


# logging info
logging.basicConfig(level=logging.DEBUG)

dbName = "../../rest_server/medisch_centrum_randstad/db.sqlite3"
tableName = "rest_api_netlify"
url = "http://localhost:8080/medish_centrum_randstad/api/netlify?page=1"
csvFile = "rest_server_new/medisch_centrum_randstad/data/data.csv"


##########################
### Read from REST API ###
##########################
# logging.info("Extract from REST API")
# response = requests.get(url)
# file_contents= response.json()  #dictionary
# logging.info("Load API Response into Pandas dataframe")
# df = pd.DataFrame.from_dict(file_contents['data'])
# #all the needed info was condensed into one data column called 'data'
# df3 = df.copy() #keep original for df3 
# logging.debug(df.head())
# logging.info("Load dataset in Database")


######################
### Read from .csv ###
######################
# df pd.read_csv('csvFile',skipinitialspace=True)
# df3 = df.copy() #keep original for df3
# logging.info("Load dataset in Database")


############################
### Read from SQlite3 db ###
############################

## saving the new df to SQL
dbConnection = sqlite3.connect(dbName)

# query db and write to pd:
dfFromDB = pd.read_sql_query(f"SELECT * FROM {'rest_api_netlify'}", dbConnection)
# sql adds index, remove:
df = dfFromDB.drop('id', axis=1)
pd.set_option('display.max_columns', 10)
# print(df.head())


#########################
### Regulair cleaning ### 
#########################

# remove negative values
df = df[(df >= 0).any(axis=1)]

# remove duplicates
df = df.drop_duplicates()

# convert non numeric to NaN
df = df.apply(lambda y: pd.to_numeric(y, errors='coerce') if y.dtype == 'object' else y)
df = df.apply(lambda y: pd.astype('float64') if y.dtype == 'object' else y)

# remove NaN
df = df.dropna()

# Add BMI
df['BMI'] = round(df['mass'] / (df['length'] / 100) ** 2, 1)



########################
### DF1 base dataset ### 
########################

df1 = df.drop(['BMI'], axis=1).copy()


df1.to_sql('df1', if_exists='replace', con=dbConnection)
print('Generated DF1: successfully written to SQL database')
df1.to_csv('df1.csv')
print('Generated DF1: successfully written to df1.csv')

############################
### DF2 enhanced dataset ### add feature 'BMI'
############################

df.to_sql('df2', if_exists='replace', con=dbConnection)
print('Generated DF2: successfully written to SQL database')
df.to_csv('df2.csv')
print('Generated DF2: successfully written to df2.csv')

########################
### CLEANING for DF3 ### outliers IQR method, BMI feature
######################## 

## the IQR clipping for outliers 
# Computing IQR
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Clipping the IQR*|15.*IQD|
mean = df.mean()
df = df.clip(lower=mean - 1.5 * IQR, upper=mean + 1.5 * IQR, axis=1)

# save to SQLlite
df.to_sql('df3', if_exists='replace', con=dbConnection)
print('Generated DF3: succesfully written to SQL database')
df.to_csv('df3.csv')
print('Generated DF3: succesfully written to df3.csv')

###################################
### Commit and close connection ###
###################################

dbConnection.commit()
dbConnection.close()
