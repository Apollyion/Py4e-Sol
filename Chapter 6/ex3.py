# Exercise 3: Encapsulate this code 
# in a function named count, and generalize it 
# so that it accepts the string and the letter as arguments.

def count(letter, word):
    count = 0
    for lt in word:
        if lt == letter:
            count = count + 1
    print(count)

word = input("Enter the word: ")
letter = input("Enter the letter: ")

count(letter, word)