# Welcome to day3 of learning python. So today we will be starting with Function and passing them with parameters. 

#============================================================== Functions =================================================

""" Function : They are the block of data. Functions are needed when we want to run a piece of code again and again"""
# Declared with a "def" keyword.

def example():
    x = 1
    y = 2
    z = x+y
    print(z)
pass


# Now this wont run since we have not called it. So for calling it we will type its function name.

example()


#----------------------------------------- Functions with Parameters ----------------------------------------------- 

# Parametersare important when we want to shorten our code and make it simple and elegant.

def additon(x,y):
    z = x+y
    print(z)

additon(5,5)

# Clearly there is no limit to the number of prameters you pass. It could be anything.

def addition(x,y,z,a):
    b = x+y+z+a
    return b

x= addition(2,3,5,8)
print(x)

#---------------------------------------------Global and Local variables -----------------------------------------

""" Global : These are the variables whose scope lies outside the function also.
Local : These variable scope lies inside the function. Using them outside the scope of function gives declaration error.
"""

z= 3

# This is global variable.

def add():
# This is local variable.  
    y = 5
    print(y)

add()
print(z)

# Let try printing y(Local variable) outside the function.


def add():
# This is local variable.  
    y = 5
    print(y)

add()
print(z)
print(y)
