def main_menu():

#	legaloption = {1: 'Review past expenses', 2: 'Make a new entry', 3: 'Visualize my activies', 4: 'Give me some Advice'}

	while True:
		ans = input("What would you like to do today?\n1. Review past expenses\n2. Make a new entry\n3. Visualize my activies\n4. Give me some Advice\nPlease enter the number: ")
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
				
main_menu()

def add_expenses():

	while True:
		exp = input("What kind of expense are you adding?\n1. Grocery\n2. Restaurant\n3. Clothes\n4. Entertainment\n5. E-devices\n6. Travel\n7. Loans\n8. Housing & Bills\n9. Others\nPlease enter the number: ")
		try:
			exp = int(exp)
		except ValueError:
			print("Not an integer. Please try again.")
		else:
			if exp not in range(1, 10):
				print("Invalid option. Please try again.")
				continue
			else:
				return exp
				break

add_expenses()