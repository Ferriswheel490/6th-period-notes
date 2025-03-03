

#helper function
def is_int(user_input):
    try:
        int(user_input)

    except:
        print("really that is not a number just give me an number")
        user_input = is_int(input("How old are you\n"))

    else:
        return int(user_input)
    
def age():
    old = is_int(input("How old are you\n"))

    print(f"wow you are {old} years old")

age()

def add(a):
    b = input("Give me a number")

    def addition():
        print(a+b)
    addition()
#add(3)

import logging

logging.basicConfig(level=logging.INFO)

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"executing {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def adder(a,b):
    return a+b
print(add(3,4))