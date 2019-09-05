# 1. write a function called add that accepts two arguments and returns their sum
# 1. write a function called subtract that accepts two arguments and returns the difference
# 1. write a function called calculate that accepts a function as an argument. 
# In calculate's body, it should execute that function and pass it the numbers 3 and 5
# 1. print an execution of calculate and pass it a reference to add
# 1. print an execution of calculate and pass it a reference to subtract

def add(a,b):
    return a + b

def subt(a,b):
    return a - b

def calc(thing):
    return thing(3,5)

print(calc(add))
print(f"{calc(subt)}")


def interior_decorator(func):
    def add_curtains():
        func()
        print("now my house has black and white curtains")

    return add_curtains

#Below is some code we started with. Joe added this "@" decorator function
#that appears to be putting "move_in" into "interior_decorator" without any
#extra syntax. TBH: I don't yet understand how it works or why it's necessary.

# def move_in():
#     print("My house was empty, but...")

# new_house = interior_decorator(move_in)
# new_house()

@interior_decorator
def move_in():
    print("My house was empty, but...")

move_in()