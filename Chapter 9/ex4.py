# Exercise 4: 
# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop to find who has the most messages 
# and print how many messages the person has.


#file = input("Enter a file name: ")

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

values_list = list(cat.values())
keys_list = list(cat.keys())
biggest_value = max(values_list)
index = values_list.index(biggest_value)

# value = cat.get(most[len(most)-1])


# print(list(cat.keys())[list(cat.values()).index(values_list[len(values_list)-1])])


print(str(keys_list[index]) + " " + str(biggest_value))