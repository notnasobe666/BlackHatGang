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

# A vector for w is created
N       = 10000
w_vec   = np.random.uniform(0.5, 1.5, size=N)

# empty lists for l and c is created
c_vec = np.empty(N)
l_vec = np.empty(N)

# a loop is generated to create optimal value of consumption \ 
# and labor supply given the wage

for i, w in enumerate(w_vec):
    opt = supply_problem(e,v,m,w_vec[i],t0,t1,k)
    c_vec[i] = opt[0]
    l_vec[i] = opt[1]

plt.style.use('grayscale')
plt.plot(w_vec,l_vec)
plt.plot(w_vec,c_vec)
plt.grid(True)
plt.show()

# Question 3

# A function to return the total tax revenue is created to be \
# used in following questions

def total_tax_revenue(e,v,m,t0,t1,k,N):
    total_tax_revenue = 0 
    np.random.seed(666)
    for i in range(1,N+1):
        w_i                 = np.random.uniform(0.5, 1.5)
        l_i, _, _           = supply_problem(e,v,m,w_i,t0,t1,k)
        total_tax_revenue   += (t0*w_i*l_i + t1*np.max(w_i*l_i-k,0))
        return total_tax_revenue

# Calculate the total tax revenue

T = total_tax_revenue(e,v,m,t0,t1,k,N)
print(T)

