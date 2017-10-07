import sys
sys.path.insert(0, '/anaconda/lib/python3.6/site-packages')

import pandas as pd #dataframe package
import numpy as np #Python number processor
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for plotting and styling

a1 = list(pd.date_range('20170901', periods=100))
d1=['Ayo','Hanyu','Muxuan','Yucheng']*25
d2=['ayoanimashaun@berkeley.edu','hanyu_chen@berkeley.edu','muxuan_lyu@berkeley.edu','yucheng.lin@berkeley.edu']*25
d3=d1
d4=['Ayospassword12@','Hhanyuspassword12@','Muxuansappasword12@','Yuchengspassword12@']*25
i1=[10000,10000,10000,10000]*25
np.random.seed(0)
e1=list(np.random.randint(100,150,size=100))
e2=list(np.random.randint(100,150,size=100))
e3=list(np.random.randint(100,150,size=100))
e4=list(np.random.randint(100,150,size=100))
e5=list(np.random.randint(100,150,size=100))
e6=list(np.random.randint(100,150,size=100))
e7=list(np.random.randint(100,150,size=100))
e8=list(np.random.randint(100,150,size=100))
e9=list(np.random.randint(100,150,size=100))
b1=list(np.random.randint(150,180,size=100))
b2=list(np.random.randint(150,180,size=100))
b3=list(np.random.randint(150,180,size=100))
b4=list(np.random.randint(150,180,size=100))
b5=list(np.random.randint(150,180,size=100))
b6=list(np.random.randint(150,180,size=100))
b7=list(np.random.randint(150,180,size=100))
b8=list(np.random.randint(150,180,size=100))
b9=list(np.random.randint(150,180,size=100))

Large_d={'User Name':d1,'Email Address':d2,'Name':d3}

df=pd.DataFrame(Large_d)
df['Date']=a1
df['Password']=d4
df['Total Income']=i1
df['GroceriesE']=e1
df['RestaurantsE']=e2
df['ClothingE']=e3
df['EntertainmentE']=e4
df['E-devicesE']=e5
df['TravelE']=e6
df['LoansE']=e7
df['House&BillsE']=e8
df['OthersE']=e9
df['GroceriesB']=b1
df['RestaurantsB']=b2 
df['ClothingB']=b3
df['EntertainmentB']=b4
df['E-devices']=b5
df['Travel']=b6 
df['Loans']=b7
df['House&Bills']=b8
df['Others']=b9
df.index=df['Date']
df=df.drop('Date', axis=1)
print (df)
df.to_csv('fake_database.csv', sep='\t')