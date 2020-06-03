import math

def ec():
    cinput = input("Give a string: ")

    for i in range(10):
        print("Index " + "[ " + str(cinput) + " ]")
    return ec(10)
