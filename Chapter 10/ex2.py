# Exercise 2: 
# This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the "From" line by finding the time string and then splitting 
# that string into parts using the colon character. Once you have accumulated the counts for each hour, 
# print out the counts, one per line, sorted by hour as shown below.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008


#file = input("Enter a file name: ")

file = "mbox-short.txt"

try:
    fhand = open(file)
except:
    print("Arquivo Invalido!")


cat = dict()
lineList = list()
subLineList = list()
t_cat =list()

for line in fhand:
    if line.startswith('From'):
        lineList = line.split()
        if len(lineList) > 2:
            subLineList = lineList[5].split(":")
            cat[subLineList[0]] = cat.get(subLineList[0],0) + 1



for key, val in list(cat.items()):
     t_cat.append((key, val))

t_cat.sort()

for val,key in t_cat:
    print(str(val) + " " + str(key))