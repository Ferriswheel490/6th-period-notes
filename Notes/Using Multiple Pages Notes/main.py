#Fairus De La Cruz, Multiple Pages Notes


from calc import addition as add, subtraction as sub

#print(add())
#print(sub(20,9))

def get_user_info():
    name = input("what is your name:\n ")
    age = int(input("what is your age:\n "))
    color = input("what is your favorite color:\n ")
    return name, age, color

name, age, color = get_user_info()

print(age)