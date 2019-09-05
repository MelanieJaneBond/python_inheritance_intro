# Write a decorator function named @kids that, when placed above a function, 
# will modify the return value of that function to have "by the kids" appended 
# to the end. For example, if the decorator is above the garbage() function, 
# when you invoke the method, it should return "The garbage was taken out by 
# the kids"

def kids(func):
    def by_the_kids():
        func()
        print(f"{func()} by the kids. We think?")
    return by_the_kids

def mom(func):
    def by_mom():
        func()
        print(f"{func()} by Mom, of course...")
    return by_mom

def dad(func):
    def by_dad():
        print(f"{func()} by Dad, isn't that amazing!")
    return by_dad

@mom
def laundry():
    return "The dirty laundry was cleaned"

@dad
def garbage():
    return "The garbage was taken out"

@kids
def dust():
    return "The house was dusted"

def groom():
    return "The dog was brushed"

garbage()
laundry()
dust()

# Now write two more decorator functions named @dad and @mom and place them 
# above the functions that you want to assign to the parents. The output 
# should be appended with "by Dad" or "by Mom".