import numpy as np 
from scipy import optimize 
import matplotlib.pyplot as plt 
import math

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
w   = 0.5

# Now the model equations are defined

def x(m,w,l,t0,t1,k): 
    """x equals the optimal consumption"""

    return m + w*l - (t0*w*l + t1*max(w*l-k,0))

def utility(l,c,e,v):
    return math.log(c) - v * ((l** (1+(1/e)))/(1+ (1/e)))

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

print(f'Optimized labour supply is: {l_star:.2f}')
print(f'Optimized consumption is:  {c_star:.2f}')
print(f'Optimal utility is: {u_star:.2f}')

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

np.random.seed(4600)
PopLarge = np.random.uniform(0.5,1.5,size=10000)

def TotalTax(PopVec,e,v,t0,t1,k,m):

    N=len(PopVec)
    PopTaxes=np.zeros((N))

    for i,w in enumerate(PopVec):
        #3.3.1. Return optimal labour supply given wage from the optimiser function
        Ind_optimum=optimiser(w,e,v,t0,t1,k,m)
        IndLabour=Ind_optimum[0]
        #3.3.2. Return tax payment given the income yielded by optimal labour supply
        PopTaxes[i]=t0*w*IndLabour+t1*max(w*IndLabour-k,0)
    #3.4. Sum over all tax payments
    TotTax=sum(PopTaxes)
    return TotTax

#3.5. Call total tax functions given the array of randomly drawn wages.
TotTax0 = TotalTax(PopLarge,e,v,t0,t1,k,m)
print(f'The total tax revenue is {TotTax0:.1f}')


# Question 4
# Frisch Elasticity changed from 0.3 to 0.1
e_new = 0.1

T_new = total_tax_revenue(e_new,v,m,t0,t1,k,N)
print(f'New total tax revenue: {T_new:.2f}')


# Question 5

# Define the negative of total tax revenue
#5.1 Draw alternative vector 
PopWageS = np.random.uniform(0.5,1.5,size=100)
PopWageM = np.random.uniform(0.5,1.5,size=1000)


#5.2.1  Create a vector 'taxes' which includes 'ltax', 'ttax' and 'cutoff'
        #return the total tax for the 100, 1000 or 10000 people
def value_of_choice_tax(taxes,PopWage,w,v,m):
    
    t0 = taxes[0]
    t1 = taxes[1]
    k = taxes[2]
    return -total_tax_revenue(e,v,m,t0,t1,k,N)

#5.2.2  Define the 'taxOptimiser' function, find the tax maximising values of the vector 'taxes'.
def taxOptimiser(PopWage,e,v,m):
    
    # 5.2.3 Call solver
    initial_guess = [0.785,0.055,0.470]
    sol_case3 = optimize.minimize(
        value_of_choice_tax,initial_guess,method='Nelder-Mead',
        args=(PopWage,e,v,m))

    t0Star=sol_case3.x[0]
    t1Star=sol_case3.x[1]
    kStar=sol_case3.x[2]

    #5.2.4 Print the solution   
    print(f'Optimal lower tax rate is {t0Star:.3f}')
    print(f'Optimal upper tax rate is {t1Star:.3f}')
    print(f'Optimal cutoff income is {kStar:.3f}')
    
    return[t0Star,t1Star,kStar]

print('Optimal taxes and estimated total tax revenue, N=100')
[t0Star,t1Star,kStar]=taxOptimiser(PopWageSmall,e,v,m)
TotTaxSmall = TotalTax(PopWageLarge,e,v,t0Star,t1Star,kStar,m)
print(f'Estimated total tax revenue is {TotTaxSmall:.1f}')

print('Optimal taxes and estimated total tax revenue, N=1000')
[t0Star,t1Star,kStar]=taxOptimiser(PopWageMedium,e,v,money)
TotTaxMedium = TotalTax(PopWageLarge,e,v,t0Star,t1Star,kStar,m)
print(f'Estimated total tax revenue is {TotTaxMedium:.1f}')