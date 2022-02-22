# Exercise 1: Write a program which repeatedly 
# reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, 
# detect their mistake using try and except and print an error message and skip to the next number.


total, counter, average = 0, 0, 0

while True:

    line = input("Enter a number: ")
    if line == "done":
        break
    try:
        total = total + int(line)
        counter = counter + 1
    except:
        print("Invalid Input") 

average = total / counter
print(total, counter, average)