# Exercise 3: 
# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.


import string

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
    line = line.strip()
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', " "))
    line = line.translate(str.maketrans('', '', "\t"))
    #words = line.split()
    for letter in line:
        cat[letter] = cat.get(letter,0) + 1
total_sum = 0
for key, val in list(cat.items()):
     t_cat.append((val, key))
     total_sum = val + total_sum
t_cat.sort(reverse=True)

for key,val in t_cat:
    print((str(val) + " " + str(key)) , " - %","%f" % (int(key)/int(total_sum)))