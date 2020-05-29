# Question 1 from https://pynative.com/python-basic-exercise-for-beginners/

# Question: "Accept two integer numbers from a user and return their product and  if the product is greater than 1000, then return their sum"

# Answer:

integer1 = int(input("Enter Integer 1: "))
integer2 = int(input("Enter Integer 2: "))

def product_or_sum():
    if integer1 * integer2 >= 1000:
        return integer1 + integer2
    else:
        return integer1 * integer2
print(product_or_sum())
