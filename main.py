import pandas as pd # dataframe package
import datetime
import numpy as np # Python number processor
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for plotting and styling


def log_in():
    df = pd.read_csv('fake_database.csv')
    name = ''
    pw = ''

    # change data frame from series to list
    username = df['User Name'].tolist()
    password = df['Password'].tolist()

    while (name not in username or pw not in password):
        # Let User input username & password
        name = str(input("Please enter your username: "))
        pw = str(input("Please enter your password: "))

        # Match user input data to database
        if name in username and pw in password:
            print("Welcome!")

        elif name not in username:
            print("Wrong user name")

        elif pw not in password:
            print("Wrong password")
    return name

def main_menu():
	"""Prints the main menu, ranging from 1 to 4, which privides users with four possible operations.
	   returns the menu index"""
	print("What would you like to do today?\n1. Review past expenses\n2. Make a new entry\n3. Visualize my activies\n4. Give me some Advice\n5. Quit")
	while True:
		ans = input("Please enter the number: ")
		try:
			ans = int(ans)
		except ValueError:
			print("Not an integer. Please try again.")
		else:
			if ans not in range(1, 6):
				print("Invalid option. Please try again.")
				continue
			else:
				return ans
				break

# Review expenses
def ViewExpenseTable(Name,Date1,Date2):
    """"This function generates a table of all expenses between the two dates entered as arguments"""
    D1 = datetime.datetime.strptime(Date1, "%Y-%m-%d")
    D2 = datetime.datetime.strptime(Date2, "%Y-%m-%d")
    if D2 < D1: # compares to see if the dates given are in the right order
        raise IndexError("Please enter a valid date range")
    uniquevalues = np.unique(df[['Name']].values) # Creates an array of unique names of users
    while Name in uniquevalues: # Checks if the name passed into the function is in the database
        df1 = df.loc[df['Name'] == Name,['Date','GroceriesE','RestaurantsE','ClothingE','EntertainmentE','E-devicesE','TravelE','LoansE','House&BillsE','OthersE']]
        df1.index=df1['Date'] # Changes index to dates in a temporary dataframe
        df1 = df1.loc[Date1:Date2,] # Indexes new dataframe by Dates
        df1 = df1.drop('Date', axis=1)
        return df1
    t = df1.iloc[:1,5:].sum(axis=1)
    s = df.iloc[-1:,5:].sum(axis=1)
    if t == s:
        return ("you have no expenses to report for this period.") # Response when exepenses cannot be found for the users name
    else:
        raise ValueError("No records for Name, {0}".format(Name))

def ReviewExpense(Name,Category,Date1,Date2):
    """This function tells the user how much they have spent in a certain category over the dates given"""
    D1 = datetime.datetime.strptime(Date1, "%Y-%m-%d")
    D2 = datetime.datetime.strptime(Date2, "%Y-%m-%d")
    if D2 < D1: # compares to see if the dates given are in the right order
        raise IndexError("Please enter a valid date range")
    while Name in df[['Name']].values: # Checks if the Name argument is indeed in the Database
        df1 = df.loc[df['Name'] == Name,['Date',Category]]
        if [Date1,Date2] in df[['Date']].values: # Check if dates given are in the main dataframe
            df1.index = df1['Date'] # Indexes new dataframe by Dates
            df1 = df1.loc[Date1:Date2,]
            df1 = df1.drop('Date', axis=1)
            t = (df1[Category].iloc[-1])-(df1[Category].iloc[0]) # Calculates summed expenses by subtracting first row from last row
            return ("Between {0} and {1}, you have spent ${2} on {3}.".format(Date1,Date2,t, Category[:-1]))
        else:
            raise IndexError("Your dates are not within the range of records") # Error message when dates given aren't in dataframe
    else:
        raise ValueError("No records for Name, {0}".format(Name))

# New entry
def new_entry_index():
	"""Returns the new entry index, ranging from 1-3"""
	print("What would you like to add?\n1.Income\n2.Expenses\n3.Budget")
	while True:
		ans = input("Please enter number: ")
		try:
			ans = int(ans)
		except ValueError:
			print("Not an integer. Please try again.")
		else:
			if ans not in range(1,4):
				print("Invalid option. Please try again.")
				continue
			else:
				return ans
				break

# Adding income:
def request_income():
	"""Returns the income value"""
	while True:
		ans = input("Please enter your income for the past period: ")
		try:
			ans = float(ans)
		except ValueError:
			print("Please enter a valid income value!")
			continue
		else:
			return ans
			break

def add_income(df,income):
	"""Store income in database"""
	new_row = df[-1:].copy()
	new_row['Total Income'] = income
	new_row.to_csv('fake_database.csv', mode='a', header=False,index=False)

# Adding expenses:
def request_expenses_index():
	"""Returns the index, ranging from 1 to 9, of the expenses category."""
	print("What kind of expense are you adding?\n1. Groceries\n2. Restaurants\n3. Clothes\n4. Entertainment\n5. E-devices\n6. Travel\n7. Loans\n8. Housing & Bills\n9. Others")
	while True:
		ans = input("Please enter the number: ")
		try:
			ans = int(ans)
		except ValueError:
			print("Not an integer. Please try again.")
		else:
			if ans not in range(1, 10):
				print("Invalid option. Please try again.")
				continue
			else:
				return ans
				break

def request_expenses(index):
	"""returns the expense of the corresponding index"""
	expense_category = expense_dict[str(index)]
	while True:
		print("Please enter your expense for",expense_category,end='')
		try:
			ans = input(":")
			ans = int(ans)
			return ans
		except ValueError:
			print("Oops! That was no valid expense value. Try again...")

def add_expenses(df,index,expense):
	"""Add the expenses to the database"""
	expense_category = expense_dict[str(index)]
	new_row = df[-1:].copy()
	new_row[expense_category] = expense
	new_row.to_csv('fake_database.csv', mode='a', header=False,index=False)

# Adding budget:
def request_budget():
	"""Returns the budget value"""
	while True:
		ans = input("Please enter your budget for the next period:")
		try:
			ans = float(ans)
		except ValueError:
			print("Please enter a valid budget value!")
			continue
		else:
			return ans
			break

def add_budget(df,budget):
	new_row = df[-1:].copy()
	new_row['Budget'] = budget
	new_row.to_csv('fake_database.csv', mode='a', header=False,index=False)

name = log_in()
df = pd.read_csv('fake_database.csv')
df_individual = df.loc[df['Name'] == name]
expense_dict = {'1':'GroceriesE','2':'RestaurantsE','3':'ClothingE','4':'EntertainmentE','5':'E-devicesE','6':'TravelE','7':'LoansE','8':'Housing&BillsE','9':'OthersE'}


while True:

	layer1_index = main_menu()

	if layer1_index == 1:
	    print("Review past expenses")
	    option = ''
	    while (option not in ['a', 'b']):
		    option = input("a. View Expense Table\nb. View Specific Category of Expense\n")
		    if option == 'a':
		        date1 = input("Please enter start date (yyyy-mm-dd): ")
		        date2 = input("Please enter end date (yyyy-mm-dd): ")
		        print(ViewExpenseTable(name,date1,date2))
		        break
		    elif option == 'b':
		        Category = input("Expense categories:\nGroceries  Restaurants  Clothing  Entertainment  \nE-devices  Travel  Loans  House&Bills  Others\nPlease choose expense category: ")
		        date1 = input("Please enter start date(yyyy-mm-dd): ")
		        date2 = input("Please enter end date(yyyy-mm-dd): ")
		        print(ReviewExpense(name,Category+'E',date1,date2))
		        break
		    else:
		    	print("Invalid option. Please try again.")

	elif layer1_index == 2:
	    print("Make a new entry")
	    entry_index = ''
	    while (entry_index not in [1,2,3]):
		    entry_index = new_entry_index()
		    if entry_index == 1:
		        income = request_income()
		        add_income(df_individual,income)
		        print("Income added!")
		        break
		    elif entry_index == 2:
		        expenses_index = request_expenses_index()
		        expense = request_expenses(expenses_index)
		        add_expenses(df_individual,expenses_index,expense)
		        print("Expense added!")
		        break
		    elif entry_index == 3:
		        budget = request_budget()
		        add_budget(df_individual,budget)
		        print("Budget added!")
		        break
		    else:
		    	print("Invalid option. Please try again.")

	# elif layer1_index == 3:

	# elif layer1_index == 4:

	elif layer1_index == 5:
		print("Have a good one!")
		break

# else: