# p1
Health Marketing

In the Health Marketing project we trained a Machine Learning model on several independant variables, like exercies and smoking. We also calculated the body mass index (bmi) based on the weight and length of a person.

Data was completely anonimized for privacy purposes, but this has it's effect on the quality of the model.

p1/notebooks
The project was built in 7 steps, displayed on a Trello board. All steps including analysis and explanantion were carried out in Jupyter notebooks.

After that a data pipleine, a regression model and an interface were build.

p1/broncode/build/pipeline_data_model_production.py:
The pipeline requests data from a REST api server and saves it to a SQLite database. 

p1/brondocde/build/pipeline_regression_model_production.py:
A regression model is trained on this data and the trained model is saved as a pickle file.

p1/broncode/run/interface.py:
The interface program for use by the health consultant loads the trained model from the pickle file and asks for user input to calculate the lifespan and the bmi.

Alternatively the coefficients and the intercept, decribing the trained model, are saved to a SQLite database, to be used by an app on a mobile phone. This is because the app isn't running on the Python programming language and therefore cannot use the trained model.

This interface.py has an improved version, called:
command_interface_production.py
This is a Work In Progress, as many improvements can still be done.
As described in the advies/Presentatie p1.pptx


p1/advies/Presentatie p1.pptx
A powerpoint with a brief report including advice and ethics.

p1/onderbouwing
A longer report   

p1/git-historie
The git history

