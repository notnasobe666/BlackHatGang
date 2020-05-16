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

Inv_X_X_trans = np.linalg.inv(X_trans_X)
Inv_X_X_trans


X_trans_y = X_trans.dot(y)
X_trans_y

beta_hat = Inv_X_X_trans.dot(X_trans_y)
betas = pd.DataFrame({'Beta 0':beta_hat,'Beta 1':beta_hat,'Beta 2':beta_hat})
betas

#######################################################################################

