import sys
# sys.path.insert(0, '/anaconda/lib/python3.6/site-packages')
import pandas as pd #dataframe package
import numpy as np #Python number processor
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for plotting and styling


df=pd.read_csv('fake_database.csv')

import datetime
def ViewExpenseTable(Name,Date1,Date2):
    """"This function generates a table of all expenses between the two dates entered as arguments"""
    D1 = datetime.datetime.strptime(Date1, "%Y-%m-%d")
    D2 = datetime.datetime.strptime(Date2, "%Y-%m-%d")
    if D2<D1: #compares to see if the dates given are in the right order
        raise IndexError("Please enter a valid date range")
    uniquevalues = np.unique(df[['Name']].values)  #Creates an array of unique names of users
    while Name in uniquevalues: #Checks if the name passed into the function is in the database
        df1=df.loc[df['Name']==Name,['Date','GroceriesE','RestaurantsE','ClothingE','EntertainmentE','E-devicesE','TravelE','LoansE','House&BillsE','OthersE']]
        df1.index=df1['Date']  #Changes index to dates in a temporary dataframe
        df1=df1.loc[Date1:Date2,] #Indexes new dataframe by Dates
        df1=df1.drop('Date', axis=1)
        return df1
    t=df1.iloc[:1,5:].sum(axis=1)
    s=df.iloc[-1:,5:].sum(axis=1)
    if t==s:
        return ("you have no expenses to report for this period.")#Response when exepenses cannot be found for the users name
    else:
        raise ValueError("No records for Name, {0}".format(Name))

def ReviewExpense(Name,Category,Date1,Date2):
    """This function tells the user how much they have spent in a certain category over the dates given"""
    D1 = datetime.datetime.strptime(Date1, "%Y-%m-%d")
    D2 = datetime.datetime.strptime(Date2, "%Y-%m-%d")
    if D2<D1: #compares to see if the dates given are in the right order
        raise IndexError("Please enter a valid date range")
    while Name in df[['Name']].values: #Checks if the Name argument is indeed in the Database
        df1=df.loc[df['Name']==Name,['Date',Category]]
        if [Date1,Date2] in df1[['Date']].values: #Check if dates given are in the main dataframe
            df1.index=df1['Date'] #Indexes new dataframe by Dates
            df1=df1.loc[Date1:Date2,]
            df1=df1.drop('Date', axis=1)
            t=(df1[Category].iloc[-1])-(df1[Category].iloc[0])#Calculates summed expenses by subtracting first row from last row
            return ("Between {0} and {1}, you have spent ${2} on {3}.".format(Date1,Date2,t, Category[:-1]))
        else:
            raise IndexError("Your dates are not within the range of records") #Error message when dates given aren't in dataframe
    else:
        raise ValueError("No records for Name, {0}".format(Name))
