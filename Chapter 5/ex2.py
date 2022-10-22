# Exercise 2: Write another program that prompts for a list of
# numbers as above and at the end prints out both the maximum
# and minimum of the numbers instead of the average.

numbers = list()


def maximum(number_list: list):
    biggest = None
    for number in number_list:
        if biggest is None or number > biggest:
            biggest = number
        # print("Current Biggest: ", biggest)
    print("Biggest Value: ", biggest)


def minimum(number_list: list):
    smallest = None
    for number in number_list:
        if smallest is None or number < smallest:
            smallest = number
        # print("Current Smallest: ", smallest)
    print("Smallest Value: ", smallest)


print("[If over, type Done]")

while True:

    try:
        value = input("Enter the number: ")
        if value == "Done":
            maximum(numbers)
            minimum(numbers)
            break
        numbers.append(float(value))
    except ValueError:
        print("Invalid Input")
