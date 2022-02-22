# Exercise 1: Write a while loop that starts 
# at the last character in the string and works 
# its way backwards to the first character in the string, 
# printing each letter on a separate line, except backwards. 

line = input("Enter with a string: ")
i = 1
while i <= (len(line)):
    print(line[-i])
    i = i + 1