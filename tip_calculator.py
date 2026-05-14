print("Welcome to the tip calculator!")
bill = float (input("Enter the billing amount: $"))
tip = int (input("choose the tip with out percentage sign please: 10% , 15%, 20%: "))
people = int(input("Enter the number of people: "))
tip_on_bill= bill*(tip/100)
your_payment= round((bill + tip_on_bill)/people , 2)
print(f"your_payment is $ {your_payment}")

