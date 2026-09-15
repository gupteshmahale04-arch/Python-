# # Section B: Coding Questions
# 1 Smart Temperature Converter
# Take input in Celsius and print its equivalent in Fahrenheit and Kelv
# (Use explicit type conversion and arithmetic operators.)
# Formula:
# · Fahrenheit = (C x 9/5) + 32
# · Kelvin = C + 273.15
tempr_= ( input( "Enter the Temperature (in Celsius ::)" ))

tempr_c = float(tempr_)

tempr_f = (tempr_c*9/5) + 32
 
print( "  Temperature in Fahrenheit : " , tempr_c)
 
tempr_K = tempr_c + 273.15 

print( "Temperature in Fahrenheit :" , tempr_K)

# 2 Bill Split Calculator
# Write a program that takes total bill amount and number of friends as input.
# Calculate how much each person will pay.
# Also print the data type of each variable used.
# (Hint: use float() and division operator)

B=input(" Enter  total  bill amount  ::"  )

print("data type Bill  amoun ::", B , type(B))

P=input(" Enter the  person :: " )

print("data type of Person ::", P, type(P))

BillA=float(B)

Person= float(P)


Calculator=BillA/Person

print("Bill Split amount :: " ,  Calculator)

print("data type of Bill Split amoun ::", Calculator)


