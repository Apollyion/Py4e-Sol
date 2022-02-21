# Exercise 2: Rewrite your pay program using try and except 
# so that your program handles non-numeric input gracefully 
# by printing a message and exiting the program. 

try:
    hours = int(input("Enter Hours: "))
except:
    print("Enter Numeric Valures")
    quit()

try:
    rate = float(input("Enter rate: "))
except:
    print("Enter Numeric Valures")
    quit()

print("Pay: " + str(hours * rate))
