#Objective: Use sckitit learn module (and its least squares model, LInearRegression) to solve simple linear regression coefficients
#The data set is the same data set used for the normal equation / matrix multiplication in a different code set

#import modules
import pandas as pd
from sklearn.linear_model import LinearRegression



#Extract regression data and place into dataframe

#create empty data frame object
df = pd.DataFrame()
#add two columns to data frame (note there are multiple ways to accomplish this)
#assume all values are training data.  For simplicity, no application of splitting data into test and train sub-sets
df["X"] = 4,5,7,9,10,12,6,9,11,13,3,5,6,7,10,14,4,5,8,8,12,13
df["y"] = 11.5,14.3,17.4,21.6,21.8,26.9,15.3,22.3,27.8,29.8,9.5,12.3,15.1,17.6,24.8,34.3,11.3,13.4,18.0,19.4,27.5,30.8



#create and fit a linear model object
#create "empty" object
lm_example = LinearRegression()

#"fit" linear model to data
lm_example.fit(df["X"].values.reshape(-1,1),df["y"].values.reshape(-1,1))

#summarize the linar model coefficients
print()  #using print empty line instead of \n
print(f"A linear regression model has been fitted for provided X and y values  \nIts intercept (x0) is {lm_example.intercept_} and its only coefficient (x1) is {lm_example.coef_}")

#summarize the coefficients as a dataframe table
coef_df = pd.DataFrame()
coef_df["intercept (xo)"] = lm_example.intercept_
coef_df["x1"] = lm_example.coef_ 
print("\nBesides printing, these values can be stored in a DataFrame table, lists, etc.  See DataFrame table below:")  #using \n to print empty line
print(coef_df)


#use linear model object to predict a value for a given set of x1 values
#create a list of x1 values
x1_forPrediction = [3,5,7.5]

#iterate through each value in prediction list
print()
print("Using these coefficients, predictions can be made.  For example,")
for i in range(len(x1_forPrediction)):
    temp = lm_example.predict([[x1_forPrediction[i]]])
    print(f"For x1 value = {x1_forPrediction[i]}, the predicted y = {temp}")
