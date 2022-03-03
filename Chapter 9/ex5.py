# Exercise 5:
# This program records the domain name (instead of the address) 
# where the message was sent from instead of who the mail came from 
# (i.e., the whole email address). At the end of the program, 
# print out the contents of your dictionary.


# file = input("Enter a file name: ")
file = "mbox-short.txt"
try:
    fhand = open(file)
except:
    print("Arquivo Invalido!")


cat = dict()
lineList = list()
x = list()
for line in fhand:
    if line.startswith('From'):
        lineList = line.split()
        if len(lineList) > 2:
            x = lineList[1].split("@")
            cat[x[1]] = cat.get(x[1],0) + 1

print(cat)