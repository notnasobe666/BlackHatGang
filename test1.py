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

# A function to return the total tax revenue is created
np.random.seed(4600)
PopulationWageLarge = np.random.uniform(0.5,1.5,size=10000)

def TotalTax(PopulationWageVec,e,v,t0,t1,k,m):

#Return an array for individual tax payments
    N=len(PopulationWageVec)
    PopulationTaxes=np.zeros((N))

    for i,w in enumerate(PopulationWageVec):
        #Return optimal labour supply given optimize functions in Q1
        Ind_optimum=supply_problem(e,v,m,w,t0,t1,k)
        IndLabour=Ind_optimum[0]
        #Optimal invidual taxpayment with optimal labor
        PopulationTaxes[i]=t0*w*IndLabour+t1*max(w*IndLabour-k,0)
    #Sum
    TotTax=sum(PopulationTaxes)
    return TotTax

#Total tax functions with random uniform dis.
TotTax0 = TotalTax(PopulationWageLarge,e,v,t0,t1,k,m)
print(f'The total tax revenue is {TotTax0:.1f}')



# Question 4
# Frisch Elasticity changed from 0.3 to 0.1
e_new = 0.1

TotTax_e_new = TotalTax(PopulationWageLarge,e_new,v,t0,t1,k,m)
print(f'The total tax revenue is {TotTax_e_new:.1f}')


# Question 5
PopulationWageSmall = np.random.uniform(0.5,1.5,size=100)
PopulationWageMedium = np.random.uniform(0.5,1.5,size=1000)

def value_of_choice_tax(taxes,PopulationWage,e,v,m):
    
    t0 = taxes[0]
    t1 = taxes[1]
    k = taxes[2]
    return -TotalTax(PopulationWage,e,v,t0,t1,k,m)

#Finds the tax maximising values of the vector 'taxes'.
def taxOptimiser(PopulationWage,e,v,m):
    
    # 5.2.3 Call solver
    initial_guess = [0.8,0.6,0.5]
    sol_case3 = optimize.minimize(
        value_of_choice_tax,initial_guess,method='Nelder-Mead',
        args=(PopulationWage,e,v,m))

    t0Star=sol_case3.x[0]
    t1Star=sol_case3.x[1]
    kStar=sol_case3.x[2]

    #Print the solution   
    print(f'Optimal standard income tax rate is {t0Star:.3f}')
    print(f'Optimal top bracet tax rate is {t1Star:.3f}')
    print(f'Optimal cut-off income is {kStar:.3f}')
    
    return[t0Star,t1Star,kStar]

print('Optimal taxe rates and revenue, with N=100')
[t0Star,t1Star,kStar]= taxOptimiser(PopulationWageSmall,e,v,m)
TotTaxSmall = TotalTax(PopulationWageLarge,e,v,t0Star,t1Star,kStar,m)
print(f'Total tax revenue = {TotTaxSmall:.2f}')

print('Optimal taxe rates and revenue, with N=1000')
[t0Star,t1Star,kStar]=taxOptimiser(PopulationWageMedium,e,v,m)
TotTaxMedium = TotalTax(PopulationWageLarge,e,v,t0Star,t1Star,kStar,m)
print(f'Total tax revenue = {TotTaxMedium:.2f}')

#print('Optimal taxe rates and revenue, with N=10000')
#[t0Star,t1Star,kStar]=taxOptimiser(PopulationWageLarge,e,v,m)
#TotTaxLarge = TotalTax(PopulationWageLarge,e,v,t0Star,t1Star,kStar,m)
#print(f'Total tax revenue = {TotTaxLarge:.2f}')