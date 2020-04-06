#####################################################################################################################
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# autoreload modules when code is run
%load_ext autoreload
%autoreload 2

# local modules
import dataproject
#####################################################################################################################

# A. load data without unnecessary data
raw_input = pd.read_csv('PL_all_seasons.csv', \
usecols=['Date','HomeTeam','AwayTeam','FTR','B365H','B365D','B365A'])

# B. convert date from string to datetimes
raw_input['Date'] = pd.to_datetime(raw_input['Date'], dayfirst = True)


# C. Add a new column named 'season' 
Type_new = pd.Series([])

# running a for loop and asigning some values to series 
for i in range(len(raw_input)): 
    if raw_input["Date"][i] < datetime(2010, 8, 10): 
        Type_new[i]="09/10"
  
    elif raw_input["Date"][i] < datetime(2011, 8, 10): 
        Type_new[i]="10/11"
  
    elif raw_input["Date"][i] < datetime(2012, 8, 10):  
        Type_new[i]="11/12"
  
    elif raw_input["Date"][i] < datetime(2013, 8, 10):  
        Type_new[i]="12/13"
  
    elif raw_input["Date"][i] < datetime(2014, 8, 10):  
        Type_new[i]="13/14"
    
    elif raw_input["Date"][i] < datetime(2015, 8, 10):  
        Type_new[i]="14/15"
  
    elif raw_input["Date"][i] < datetime(2016, 8, 10):  
        Type_new[i]="15/16"

    elif raw_input["Date"][i] < datetime(2017, 8, 10):  
        Type_new[i]="16/17"
  
    elif raw_input["Date"][i] < datetime(2018, 8, 10):  
        Type_new[i]="17/18"
  
    elif raw_input["Date"][i] < datetime(2019, 8, 10):  
        Type_new[i]="18/19"

    else: 
        season[i]= raw_input["Date"][i] 
  
        
        # inserting new column with values of list made above         
raw_input.insert(2, "Season", Type_new) 

#####################################################################################################################

# D. add boolean of result Home, Draw, Away
df = pd.DataFrame(raw_input)
df['H_true'] = df['FTR'].str.count("H")
df['D_true'] = df['FTR'].str.count("D")
df['A_true'] = df['FTR'].str.count("A")

#####################################################################################################################

# E. Calculate return for every bet
df['Return_D'] = df.D_true * df.B365D
df['Return_A'] = df.A_true * df.B365A
df['Return_H'] = df.H_true * df.B365H

#####################################################################################################################

# F. Group by seasons
Season_group = df.groupby(['Season','FTR']).sum()
drop_these = ['B365H','B365D','B365A']
Season_group.drop(drop_these, axis=1, inplace=True)

#####################################################################################################################

# G. Order the grouped dataframe
Season_group['BetW'] = Season_group.H_true + Season_group.D_true + Season_group.A_true
Season_group['BetR'] = Season_group.Return_H + Season_group.Return_D + Season_group.Return_A

#####################################################################################################################

# H. Final dataframe
Bets = pd.DataFrame(Season_group, columns=['BetW', 'BetR'])
Bets['NetNomR'] = Bets.BetR - 380
Bets['Return_pct'] = (Bets.BetR / 380 -1)
Bets['Return_pct'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Bets['Return_pct']],index = Bets.index)
Bets

#####################################################################################################################

# I. visual presentation
Vis = df.groupby('Season').sum()
Vis['D_pct'] = (Vis.Return_D / 380 - 1)*100
Vis['A_pct'] = (Vis.Return_A / 380 - 1)*100
Vis['H_pct'] = (Vis.Return_H / 380 - 1)*100
Vis

# Draw graph
Vis.D_true.plot.bar()
Vis.D_pct.plot(secondary_y=True,color='r')
plt.show()


Away = plt.plot(y=['A_true','A_pct'])
Home = plt.plot(y=['H_true','H_pct'])

y1_draw = ['D_true']
y2_draw = ['D_pct']





