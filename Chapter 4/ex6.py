# Exercise 6: Rewrite your pay computation with time-and-a-half
# for overtime and create a function called computepay 
# which takes two parameters (hours and rate).


def computepay(hours, rate):
    if(hours > 40):
        print("Pay: " + str(round((hours*rate)*1.5,2)))
    else:
        print("Pay :" + str(round((hours*rate),2)))

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

computepay(hours,rate)