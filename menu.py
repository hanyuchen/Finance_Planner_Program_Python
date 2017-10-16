def main_menu():

#	legaloption = {1: 'Review past expenses', 2: 'Make a new entry', 3: 'Visualize my activies', 4: 'Give me some Advice'}
	"""Prints the main menu, ranging from 1 to 4, which privides users with four possible operations.
	   returns the menu index"""
	print("What would you like to do today?\n1. Review past expenses\n2. Make a new entry\n3. Visualize my activies\n4. Give me some Advice")
	while True:
		ans = input("Please enter the number: ")
		try:
			ans = int(ans)
		except ValueError:
			print("Not an integer. Please try again.")
		else:
			if ans not in range(1, 5):
				print("Invalid option. Please try again.")
				continue
			else:
				return ans
				break

# new entry
def new_entry_index():
	"""Returns the new entry index, ranging from 1-3 """
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
# if income:
def request_income():
	"""Returns the income value """
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

#test add: below is for testing
# import pandas as pd
# df = pd.read_csv('fake_database.csv')
# add_income(df,1000)

# if expenses:
def request_expenses_index():
	"""Returns the index, ranging from 1 to 9, of the expenses category. """
	print("What kind of expense are you adding?\n1. Grocery\n2. Restaurant\n3. Clothes\n4. Entertainment\n5. E-devices\n6. Travel\n7. Loans\n8. Housing & Bills\n9. Others")
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

expense_index = {'1':'Grocery','2':'Restaurant','3':'Clothes','4':'Entertainment','5':'E-devices','6':'Travel','7':'Loans','8':'Housing & Bills','9':'Others'}

def request_expenses(index):
	"""returns the expense of the corresponding index"""
	expense_category = expense_index[str(index)]
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
	expense_category = expense_index[str(index)]
	new_row = df[-1:].copy()
	new_row[expense_category] = expense
	new_row.to_csv('fake_database.csv', mode='a', header=False,index=False)

# if budget:
def request_budget():
	"""Returns the budget value """
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



