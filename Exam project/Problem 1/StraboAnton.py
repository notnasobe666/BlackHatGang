# Linear regression

# packagaes 
import numpy as np 
import pandas as pd

# y_i = beta0 + beta1 x1_i + beta2 x2_i + epsilon

# data generating proces - inserted from exam description
def DGP(N):
    
    # a. independent variables
    x1 = np.random.normal(0,1,size=N)
    x2 = np.random.normal(0,1,size=N)
    
    # b. errors
    eps = np.random.normal(0,1,size=N)
    
    extreme = np.random.uniform(0,1,size=N)
    eps[extreme < 0.05] += np.random.normal(-5,1,size=N)[extreme < 0.05]
    eps[extreme > 0.95] += np.random.normal(5,1,size=N)[extreme > 0.95]
    
    # c. dependent variable
    y = 0.1 + 0.3*x1 + 0.5*x2 + eps
    
    return x1, x2, y

# accessable data - inserted from exam description

np.random.seed(2020)
x1,x2,y = DGP(10000)

#######################################################################################

# To define X, x1 and x2 must be included in the same dataframe. Also a column of one's 
# for Beta_0.

x0 = 1
X = pd.DataFrame({'x0':x0,'x1':x1,'x2':x2})
X

# Question 1 

# Now X can be transposed etc by numpy formulas. 

X_trans = X.T
X_trans

X_trans_X = X_trans.dot(X)
X_trans_X
#
Inv_X_X_trans = np.linalg.inv(X_trans_X)
Inv_X_X_trans


X_trans_y = X_trans.dot(y)
X_trans_y

beta_hat = Inv_X_X_trans.dot(X_trans_y)
beta_hat

betas = pd.DataFrame({'Beta 0':beta_hat,'Beta 1':beta_hat,'Beta 2':beta_hat})
betas

#######################################################################################

# Question 2

# Lav stor fed 3D plot med beta vægte ganget på mulige forekomster af x1 og x2. 

# Plane ind som Surface

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

y_hat = np.dot(X,beta_hat)
y_hat
df_y_hat = pd.DataFrame({'x1':x1,'x2':x2,'y_hat':y_hat})
df_y_hat.head()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(df_y_hat['x1'],df_y_hat['x2'],df_y_hat['y_hat'], c='pink',marker='o',alpha=1)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y3')
plt.show

#######################################################################################

## Question 3

# præsenter i data frame

from scipy.optimize import minimize

b0 = np.empty(1)
b1 = np.empty(1)
b2 = np.empty(1)

def function(x, b0, b1, b2):

    b0 = x[0]
    b1 = x[1]
    b2 = x[2]

    return np.sum((y - (b0 + b1*x1 + b2*x2))**2)


#initial guess
b = np.array([0.2, 1.5, 9.5])

estimate = minimize(function, b, args=(b0,b1,b2), method='SLSQP')

b0 = estimate.x[0]
b1 = estimate.x[1]
b2 = estimate.x[2]

print(estimate.message)

print(b0,b1,b2)

#######################################################################################

# Question 4

# præsenter i data frame

beta_hat[0]

from scipy.optimize import minimize

b0 = np.empty(1)
b1 = np.empty(1)
b2 = np.empty(1)

def function(x, b0, b1, b2):

    b0 = x[0]
    b1 = x[1]
    b2 = x[2]

    return np.sum(np.absolute(y - (b0 + b1*x1 + b2*x2)))


#initial guess
h = np.array([0.4, 1.2, 10.5])

estimate = minimize(function, h, args=(b0,b1,b2), method='SLSQP')

b0 = estimate.x[0]
b1 = estimate.x[1]
b2 = estimate.x[2]

print(estimate.message)

print(b0,b1,b2)

#######################################################################################

# Question 5
 
# OLS
b0_OLS = np.empty(5000)
b1_OLS = np.empty(5000)
b2_OLS = np.empty(5000)

for k in range(5000):
    new_x1, new_x2, new_y = DGP(50) 
   
    def new_function(x, b0_OLS, b1_OLS, b2_OLS): 
        b0_OLS = x[0]
        b1_OLS = x[1]
        b2_OLS = x[2]

        return np.sum((new_y- (b0_OLS +  b1_OLS*new_x1 + b2_OLS*new_x2))**2)
    
    new_est = minimize(new_function, b, args=(b0_OLS,b1_OLS,b2_OLS),method = 'SLSQP')
    b0_OLS[k-1]=new_est.x[0]
    b1_OLS[k-1]=new_est.x[1]
    b2_OLS[k-1]=new_est.x[2]




# LAD
b0_LAD = np.empty(5000)
b1_LAD = np.empty(5000)
b2_LAD = np.empty(5000)

for k in range(5000):
    new_x1, new_x2, new_y = DGP(50) 
   
    def new_function(x, b0_LAD, b1_LAD, b2_LAD): 
        b0_LAD = x[0]
        b1_LAD = x[1]
        b2_LAD = x[2]

        return np.sum(np.absolute(new_y - (b0_LAD +  b1_LAD*new_x1 + b2_LAD*new_x2)))
    
    new_est = minimize(new_function, b, args=(b0_LAD,b1_LAD,b2_LAD),method = 'SLSQP')
    b0_LAD[k-1]=new_est.x[0]
    b1_LAD[k-1]=new_est.x[1]
    b2_LAD[k-1]=new_est.x[2]


# OLS & LAD beta_0 print hist 
OLS_b0_hist = plt.hist(b0_OLS,bins=50)
LAD_b0_hist = plt.hist(b0_LAD,bins=50)
plt.show(OLS_b0_hist,LAD_b0_hist)

OLS_b1_hist = plt.hist(b1_OLS,bins=50)
LAD_b1_hist = plt.hist(b1_LAD,bins=50)
plt.show(OLS_b1_hist,LAD_b1_hist)

OLS_b2_hist = plt.hist(b2_OLS,bins=50)
LAD_b2_hist = plt.hist(b2_LAD,bins=50)
plt.show(OLS_b2_hist,LAD_b2_hist)
