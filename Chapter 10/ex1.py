# Exercise 1: 
# Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary. After all the data has been read, 
# print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

#file = input("Enter a file name: ")

file = "mbox-short.txt"

try:
    fhand = open(file)
except:
    print("Arquivo Invalido!")


cat = dict()
lineList = list()
t_cat =list()

for line in fhand:
    if line.startswith('From'):
        lineList = line.split()
        if len(lineList) > 2:
            cat[lineList[1]] = cat.get(lineList[1],0) + 1

for key, val in list(cat.items()):
    t_cat.append((val, key))

t_cat.sort(reverse=True)

for key,val in t_cat[:1]:
    print(str(val) + " " + str(key))