# Exercise 3: 
# Write a program to read through a mail log, 
# build a histogram using a dictionary to count 
# how many messages have come from each email address, 
# and print the dictionary


# file = input("Enter a file name: ")
file = "mbox-short.txt"
try:
    fhand = open(file)
except:
    print("Arquivo Invalido!")


cat = dict()
lineList = list()

for line in fhand:
    if line.startswith('From'):
        lineList = line.split()
        if len(lineList) > 2:
            cat[lineList[1]] = cat.get(lineList[1],0) + 1

print(cat)