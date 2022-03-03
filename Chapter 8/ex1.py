# Exercise 1:
# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list 
# that contains all but the first and last elements.

letters = ['a', 'b', 'c',"d","e","f","g","h"]

def chop(t):
    t.pop(0)
    t.pop(len(t)-1)
    return None

def middle(t):
    t = t[1:(len(t)-1)]
    return t

print(letters)
chop(letters)
print(letters)
middle_letters = middle(letters)
print(letters)
print(middle_letters)
