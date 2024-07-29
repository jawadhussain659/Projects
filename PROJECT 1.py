# customer name 
customer_name = input("Enter customer name: ")

# bill amount
bill_amount = float(input("Enter bill amount: "))

# calculate tip which is 10%
tip = bill_amount * 0.10

# calculate gst which is 20%
gst = bill_amount * 0.20

# calculate total bill amount included tip and gst
total_bill = bill_amount + tip + gst

# printing total bill
print(total_bill)

# taking input from user about cash which is given by customer
cash = float(input("Enter the amount of cash given: "))

# calculating change which is amount of cash given minus total bill amount
change = cash - total_bill  

# printing proper bill

# printing customer name
print(f"Customer Name: {customer_name}" )

# printing bill amount
print(f"Bill Amount: {bill_amount}")

# printing tip amount
print(f"Tip (10%): {tip}")

# printing gst amount
print(f"GST (20%): {gst}")

# printing total bill amount
print(f"Total Bill: {total_bill}")

# printing cash given by customer
print(f"Cash Given: {cash}")

# printing change
print(f"Change: {change}")

# printing the thanks message
print("Thanks for visting our resturant!")  
