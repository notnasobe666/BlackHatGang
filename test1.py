import numpy as np 
from scipy import optimize 
import matplotlib.pyplot as plt 
import math as math

# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# Question 1

# Construct a function which solves eq. (1)

# first the objective is defined
def objective(x):
    c = x[0]
    l = x[1]
    v = x[2]
    e = x[3]
    return np.log(c) - v * (l**(1+(1/e)))/(1+(1/e))

# then the constraint(s) are defined

def constraint1(x):
    return m + w*l - (t0*w*l+t1*np.max(w*l-k,0)) - z

x0 = [1,1,1,1]
print(objective(x0))