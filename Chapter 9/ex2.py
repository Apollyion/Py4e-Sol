# Exercise 2:
# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with "From",
# then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).s


file = input("Enter a file name: ")

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
            cat[lineList[2]] = cat.get(lineList[2],0) + 1

print(cat)