import numpy as np 
from scipy import optimize 
import matplotlib.pyplot as plt 
import math as math

# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# Question 1

# First the global variables are defined
m = 1
v = 10 # scales the disutility of labor
e = 0.3 # Frisch elasticity
t0 = 0.4 # standard labor income tax
t1 = 0.1 # top bracket labor income tax
k = 0.4 # cut-off for the top labor income bracket
w = 0.5 # wage rate

#Defining utility function
def utility(c,l,v,e):
    u = np.log(c) - v*((l**(1+1/e))/(1+1/e))
    return u 

#Defining budget constraint
def constraint(m,w,l,t0,t1,k):
    x = m+ w*l - (t0*w*l+t1*np.max(w*l-k,0))
    return x

#plot c into x
def objective(l,w,e,v,t0,t1,k):
    c = constraint(m,w,l,t0,t1,k)
    return -utility(c,l,v,e)

def optimzer(w,e,v,t0,t1,k,m):
    res = optimize.minimize_scalar(objective, bounds=(0,1) , method='bounded', args=(w,e,v,t0,t1,k))
    l_star = res.x
    c_star = constraint(m,w,l_star,t0,t1,k)
    u_star = utility(c_star,l_star,v,e)
    return l_star, c_star, u_star

l_star = optimzer(w,e,v,t0,t1,k,m)[0]
c_star = optimzer(w,e,v,t0,t1,k,m)[1]
u_star = optimzer(w,e,v,t0,t1,k,m)[2]

print(f'Optimized labour supply is: {l_star:.2f}')
print(f'Optimized consumption is:  {c_star:.2f}')
print(f'Optimal utility is: {u_star:.2f}')

# Question 2

plt.style.use('grayscale')

# Plot l_star and c_star with w going from 0.5 to 1.5
# The definitions are defined - the used packages is defined above
N = 10000
w_vec = np.random.uniform(0.5,1.5,size=N)
c_opt = np.empty(N)
l_opt = np.empty(N)

# a loop is generated to test the range of W 

for i, w in enumerate(w_vec):
    optimization = optimzer(w,e,v,t0,t1,k,m)
    l_opt[i]=optimization[0]
    c_opt[i]=optimization[1]


fig = plt.figure(figsize=(10,5))
plt.plot(w_vec,l_opt)
plt.plot(w_vec,c_opt)
plt.grid(True)
plt.xlabel("w")
plt.ylabel("c*,l*")
plt.title("Optimal labor supply and consumption")
plt.show()

# Left plot
# axis_left = fig.add_subplot(1,2,1)
#axis_left.plot(w_vec,l_opt)
#axis_left.set_title('Optimal labor supply given w')
#axis_left.set_xlabel('$w$')
#axis_left.set_ylabel('$l$')
#axis_left.grid(True)

# Right plot 
#axis_right = fig.add_subplot(1,2,2)
#axis_right.plot(w_vec,c_opt)
#axis_right.set_title('Optimal consumption given w')
#axis_right.set_xlabel('$w1$')
#axis_right.set_ylabel('$c$')
#axis_right.grid(True)

#plt.show


# Question 3

# Calculate the tax revenue

# tax_revenue = sum(t0*w*l_star+t1 * max(w*l_star-k,0))
tax_revenue = np.sum(t0*w_vec*l_opt + t1*np.max(w_vec*l_opt-k,0))
print(f'Total tax revenue: {tax_revenue:.2f})

# Question 4

# How does the tax revenue change when e = 0.1? 
# New epsilon is defined
e_new = 0.1
l_opt_e_new = np.empty(N)

# Same loop is used as above but only a new labor
# supply is calculated as consumption isn't included
# in the tax revenue formula
for i, w in enumerate(w_vec):
    optimization = optimzer(w,e_new,v,t0,t1,k,m)
    l_opt_e_new[i]=optimization[0]

# then the new tax revenue can be calculated
tax_revenue_e_new = np.sum(t0*w_vec*l_opt_e_new + t1*np.max(w_vec*l_opt_e_new-k,0))
print(f'New total tax revenue: {tax_revenue_e_new:.2f}')

# Thus the difference in tax revenue can be calucalted as
print(f'The difference in tax revenue is: {tax_revenue_e_new-tax_revenue:.2f}')


# Question 5

# Optimize the tax 

def optimized_tax_revenue(x):
    t0 = x[0]
    t1 = x[1]
    k   = x[2]
    return -tax_revenue(e,v,m,t0,t1,k,N)

#tax optimiser
def taxopt() 



Guess = [0.2,0.3,0.4]

solution = optimize.minimize(optimized_tax_revenue,Guess,method='SLSQP',bounds=((0,1),(0,1),(0,1))))
t0  = solution.x[0]
t1  = solution.x[1]
k   = solution.x[2] 
T   = tax_revenue(e,v,m,t0,t1,k,N)

print(t0)





