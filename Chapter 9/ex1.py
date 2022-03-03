# Exercise 1: https://www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt 
# and stores them as keys in a dictionary. It doesn't matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

fhand = open("words.txt")
count = 0
wordsDict = dict()
wordlist = list()
for line in fhand:
    wordlist = line.split()
    for words in wordlist:
        wordsDict[words] = count
        count = count+1
print(wordsDict)