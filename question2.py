# Question 2 from https://pynative.com/python-basic-exercise-for-beginners/

# Question: "Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number."

# Answer:

def num(n):
    for i in range(n):
        pn = i + 1
        p = i + pn
        print("Pn: ", i, "Cn: ", pn, "Sm: ", p)
num(10)
