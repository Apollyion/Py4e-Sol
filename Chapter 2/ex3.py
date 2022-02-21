#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

print("Pay: " + str(round(rate*hours,2)))