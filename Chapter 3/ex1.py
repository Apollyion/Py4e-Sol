#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = int(input("Enter Hours: "))
rate = float(input("Enter rate: "))

if(hours > 40):
    print("Pay: " + str(round((hours*rate)*1.5,2)))
else:
    print("Pay :" + str(round((hours*rate),2)))