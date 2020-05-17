##############################################################################

#PROBLEM 2

#packages
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# import from exam description

# a. parameters
rho = 2
alpha = 0.8
beta = 0.96
r = 0.04
Delta = 0.25

# b. grids
m1_vec = np.linspace(1e-8,10,100)
m2_vec = np.linspace(1e-8,10,100)
d_vec = np.linspace(1e-8,5,100)

Lambda = 0.2
m0_vec = np.linspace(1e-8,6,100)
d0_vec = np.linspace(1e-8,3,100)

##############################################################################

# Basic function

def utility(c, d, alpha, rho):
    return

def





# Question 1 - Find and plot the functions v2, c* and x*

plt.plot(m1_vec)
plt.plot(m2_vec)
plt.plot(d_vec)

