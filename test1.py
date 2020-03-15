import numpy as np 
from scipy import optimize 
import matplotlib.pyplot as plt 
import math as math

# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# Question 1

# Construct a function which solves eq. (1)

# Following variables is known
m   = 1
v   = 10
e   = 0.3
t0  = 0.4
t1  = 0.1
k   = 0.4

# Now the model equations are defined

def x(m,w,l,t0,t1,k): 
    """x equals the optimal consumption"""

    return m + w*l - (t0*w*l + t1*np.max(w*l-k,0))

def utility(l,c,e,v):
    return np.log(c) - v * ((l** (1+(1/e)))/(1+ (1/e)))

def labor_supply(l,e,v,m,w,t0,t1,k):
    c = x(m,w,l,t0,t1,k)
    return -utility(l,c,e,v)

def supply_problem(e,v,m,w,t0,t1,k):
    solution =  optimize.minimize_scalar(labor_supply,method='bounded', \
                bounds=(0,1), args=(e,v,m,w,t0,t1,k))
    l = solution.x
    c = x(m,w,l,t0,t1,k)
    u = utility(l,c,e,v)
    return l,c,u

l_star = supply_problem(e,v,m,w,t0,t1,k)[0]
c_star = supply_problem(e,v,m,w,t0,t1,k)[1]
u_star = supply_problem(e,v,m,w,t0,t1,k)[2]

print('Optimal labour supply is: ' + str(l_star))
print(c_star)
print(u_star)

# Question 2


