#Objective: Use normal equation and matrix multiplicaiton (instead of something like gradient discent) to solve simple linear regression
#The data set is the same data set used for the scikit learn example in a different code set

#import modules
import numpy as np
import matplotlib.pyplot as plt



#Extract regression data and place into array formats for normal equation
#"Read" in a list of independent features as an array, X [Here values are given instead of being read from separate source]
X = np.array([4,5,7,9,10,12,6,9,11,13,3,5,6,7,10,14,4,5,8,8,12,13]).reshape(-1,1)

#"Read" in a list of observed output as an array, y [Here, y values are given instead of being read from separate source]
#This will be used in normal equation
y=np.array([11.5,14.3,17.4,21.6,21.8,26.9,15.3,22.3,27.8,29.8,9.5,12.3,15.1,17.6,24.8,34.3,11.3,13.4,18.0,19.4,27.5,30.8]).reshape(-1,1)

#create an array of ones that match length of array X
X_ones = np.ones(len(X)).reshape(-1,1)

#create an array that appends original x array and ones array into a feature matrix where initial column is x0 (value always equal to 1) and next column is x1
#This will be used in normal equation
X_mat = np.append(X_ones, X,axis=1)



#implement normal equation to solve for theta (coefficients)
#normal equation = (1 / (X_mat transposed * X_mat)) * (X_mat transpose * y)
Regression_Mat=np.dot(np.linalg.inv(np.dot(X_mat.T,X_mat)),np.dot(X_mat.T,y))

#Use regression to predict two values.  Two values will also be used to create regression line that is plotted against original data set
#identify min x and max x that will be x components of two x,y plots
xmin = min(X)
xmax = max(X)

#Use regression object to predict values for xmin and xmax.  These will be y components of x, y plots
ymin = Regression_Mat[0] + xmin*Regression_Mat[1]
ymax = Regression_Mat[0] + xmax*Regression_Mat[1]



#create chart with scatter points for original x features and y observed 
#modify chart style from matplotlib default
plt.style.use("seaborn")

#add scatter plot of original data set to chart
plt.scatter(X,y,label="observed data")

#add regression line to chart using two predicted values
x_plot=[xmin,xmax]
y_plot=[ymin,ymax]
plt.plot(x_plot,y_plot,color="purple",label="regression: x0 = " + str(Regression_Mat[0]) + " | x1 = " + str(Regression_Mat[1]))

#add simple chart labeling
plt.xlabel("independent or features")
plt.ylabel("dependent or observed output")
plt.legend()
plt.title("Regression using normal equation")

#show chart
plt.show()


