import numpy as np
import matplotlib.pyplot as plt
import sympy as sm 


x = "hallo"

print(3+4+5)
# stupid


def optimized_tax_revenue(x):
    t_0 = x[0]
    t_1 = x[1]
    k   = x[2]
    return -tax_revenue(e,v,m,t0,t1,k,N)

Guess = [0.2,0.3,0.4]

solution = optimize.minimize(optimized_tax_revenue,Guess,method='SLSQP',bounds=((0,1),(0,1),(0,1))))
t0  = solution.x[0]
t1  = solution.x[1]
k   = solution.x[2] 
T   = tax_revenue(e,v,m,t0,t1,k,N)

print(t0)