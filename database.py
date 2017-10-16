import sys
sys.path.insert(0, '/anaconda/lib/python3.6/site-packages')

import pandas as pd #dataframe package
import numpy as np #Python number processor
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for plotting and styling
import datetime

a1 = pd.date_range('20170901', periods=100)
d1=['Ayo','Hanyu','Muxuan','Yucheng']*25
d2=['ayoanimashaun@berkeley.edu','hanyu_chen@berkeley.edu','muxuan_lyu@berkeley.edu','yucheng.lin@berkeley.edu']*25
d3=d1
d4=['Ayospassword12@','Hhanyuspassword12@','Muxuansappasword12@','Yuchengspassword12@']*25
i1=[1000,1200,5000,7000]*25
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
b1=i1=[900,900,3000,5000]*25



Large_d={'User Name':d1,'Email Address':d2,'Name':d3}

df=pd.DataFrame(Large_d)
df['Date']=a1
df['Password']=d4
df['Total Income']=i1
df['GroceriesE']=e1
df['RestaurantsE']=e2
df['ClothingE']=e3
df['EntertainmentE']=e4
df['E_devicesE']=e5
df['TravelE']=e6
df['LoansE']=e7
df['House_BillsE']=e8
df['OthersE']=e9
df['Budget']=b1
df['Date'] = pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.to_period('M')

df['GroceriesSum']= df.groupby(['Name', 'Month']).GroceriesE.cumsum()
df['RestaurantsSum']=df.groupby(['Name', 'Month']).RestaurantsE.cumsum()
df['ClothingSum']=df.groupby(['Name', 'Month']).ClothingE.cumsum()
df['EntertainmentSum']=df.groupby(['Name', 'Month']).EntertainmentE.cumsum()
df['E-devicesSum']= df.groupby(['Name', 'Month']).E_devicesE.cumsum()
df['TravelSum']=df.groupby(['Name', 'Month']).TravelE.cumsum()
df['LoansSum']=df.groupby(['Name', 'Month']).LoansE.cumsum()
df['House&BillsSum']=df.groupby(['Name', 'Month']).House_BillsE.cumsum()
df['OthersSum']=df.groupby(['Name', 'Month']).OthersE.cumsum()


df.to_csv('fake_database.csv', sep=',', header=True, index=False)