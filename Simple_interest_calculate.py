#Sahil Patel
#Simple Interest Loan Calculate 

total_interest_paid = 0
total_cost = 0


def loan(principal, interest, term):
        
	interest = interest / (100 * 12)
	total_num_of_payments = term * 12
	a = (principal * interest * ((1 + interest) ** total_num_of_payments))
	b = ((1 + interest) ** total_num_of_payments - 1)
	c = a / b
	total_interest_paid = (c * total_num_of_payments) - principal
	total_cost = c * total_num_of_payments
	print("Principal on the loan is $" + format(principal, "7,d"))
	print("The monthly payment is $ " + format((total_cost / total_num_of_payments), "7,.2f"))  
	print("The total interest for the loan is $ " + format(total_interest_paid, "7,.2f") )
	print("The total number of payments is " + str(total_num_of_payments))
	print("The total cost of the loan is $ " + format(total_cost, "7,.2f"))

#Enter Principal, Interest as a whole or a decimal number, and term in years
"""
Example:
Principal: $80,000
Interest: 4 means 4 % (percent)
Term: 3 (in years)
Parameters should be given in this order: loan(principal, rate, years)
so, the function input looks like this: loan(80000,4,3)
"""
loan(1000000,4,2)




