# Hello Guys welcome to the day 2 of Python tutorial... Now today we will be covering variables, loops and conditionals.

#==================================================================1. Variables ===========================================

# A "Variable" is used to store values in it. This allocates memory to the system and allows further opeartion to carry on.
# Eg:- ab = 10

#The good part about python is you dont need to define whether it is int or float.

a = 10
b = 20 
c = a+b
print(c)

# It can also be overwritten.

c = a-b
print(c)

c = a*b
print(c)

c = (a)/b
print(c)

a = "Maria"
print(a)

""" Condition for Variable names in Python.
1.> A variable is a memory location where a programmer can store a value. Example : roll_no, amount, name etc.
2.> Value is either string, numeric etc. Example : "Sara", 120, 25.36
3.> Variables are created when first assigned.
4.> Variables must be assigned before being referenced.
5.> The value stored in a variable can be accessed or updated later.
6.> No declaration required
7.> The type (string, int, float etc.) of the variable is determined by Python
8.> The interpreter allocates memory on the basis of the data type of a variable.
"""

#============================================================ Loops ================================================

#  A loop is a programming structure that repeats a sequence of instructions until a specific condition is met. Programmers use loops to cycle through values, add sums of numbers, repeat functions, and many other things.

""" It is of three types.

1.> While loop
2.> For loop
"""

#-------------------------------------------------------- While --------------------------------------------------------
# Remeber there is a perfect syntax for loops or conditionals in Python. Since there is no break so we need to follow them and that is giving four spaces in next line.

a = 1
while a<10:
    print(a)
    a += 1

# Now this will print upto 9 since the condition given is upto 9. With each iteration it will check the condition and upon successful check it will return the output. 
# The thing about whille is that it will always print the first iteration.

#-----------------------------------------------------For Loop-----------------------------------------------------------

example = [1,2,35,8,9,5]
for thing in example:
    print(thing)

# So this would loop over to the list that we have entered. This would further print them in next line.

# Range function:  It sets the value from initial to end. The end value is excluded.

for i in range(0,10): 
    print(i)

# This would print from 0 to 9. 10 is the end value so it will be excluded.
 

#============================================= Conditionals ============================================================

# These are generally decision making. They decide which block of statement to run based on few conditions passed. If evaluated to true the if block runs else the else block runs.
 
"""
It consists of three parts :
1. If statement.
2. Else-if statement.
3. If-elif-else statement.   
"""

#-----------------------------------------If statement-------------------------------------------------------------------

# depends on condition and execues a block of statement. If evaluates to true then a set of if statement is executed. LEts check this in demo.

a = 2
b = 3

if(a>b) : 
    print("a is greater")
if(a<b) :
    print("b is greater")
pass

#The output will be B is greater since it greater and evaluates to true.

#----------------------------------------------- Else-if statement -------------------------------------------------------------


a = 3
b = 2

if(a>b) : 
    print("a is greater")
else :
    print("b is greater")
pass

# Now the else consists of all the remaining cases.

#--------------------------------------------If-Elif-Else statement-------------------------------------------------------------


a = 3
b = 2
c= 5

if(a>b and a>c) : 
    print("a is greater")
elif (b>a and b>c):
    print("b is greater")
else:
    print("c is greater")
pass

# Now this is used for multiple statements passing. All the conditions are statement of blocks where the true block will be executed and false will be terminated.


