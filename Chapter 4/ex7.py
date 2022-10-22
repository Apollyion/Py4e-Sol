# Exercise 7: Rewrite the grade program from the 
# previous chapter using a function called 
# compute_grade that takes a score as its
# parameter and returns a grade as a string.

def compute_grade(grade: float):
    if 0.9 <= grade <= 1:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    elif grade < 0.6:
        print("F")


try:
    while True:
        try:
            score = float(input("Enter Score: "))
            if score > 1:
                raise ValueError("Bad Score!")
            compute_grade(score)
        except ValueError:
            print("Bad Score!")
except KeyboardInterrupt:
    print("Exiting...")
