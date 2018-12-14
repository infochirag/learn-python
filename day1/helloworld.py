# Hello and welcome to Week 1 of Python Classes !! My name is Chirag Gupta. Let's get started.

# Here we wil be covering the very basics of Python which will include Printing and some operations of Strings.

# Ohh and BTW this '#' symbol is used for multi line comment.

""" This is 
 a multi line 
    comment """ 

#=======================================================Basic : Playing with string =============================================


# 1. This will print some text in print statement.
  
print(' Hello World !')

#2. Actually python supports double, single and triple quotes. 

print(" Hello world !")


#3. Unlike C or C++ we can add strings directly, which is also called concatenation.

print('concat' + 'enation')

# Ques.> Try to print your name with concatenation and give spaces between name.

#4. We can even add it with numbers

# print('I am' + 5)

# But doing this would generate and error because Python can't addstring with number so for that we need to convert number into string with 'str' function.

print('I am' + ' ' + str(5))


#====================================================== Playing with numbers ========================================================

""" Types of Operator
Python language supports the following types of operators.

1.> Arithmetic Operators
2.> Comparison (Relational) Operators
3.> Assignment Operators
4.> Logical Operators
5.> Bitwise Operators
6.> Membership Operators
7.> Identity Operators """

#------------ 1.> Arithmetic operator : ---------------------

# a.) Addition: Add two numbers
print(1+1)
print(2+8)

# b.) Subtraction: Subtracts two numbers 
print(1-1)
print(2-8)

# c.) Multiply: Multiplies two numbers 
print(1*1)
print(2*8)

# d.) Division: Divides two numbers 
print(1/1)
print(2/8)

# e.) Floor Division (//): Gives the floor value when dividing. 
print(1//1)
print(2//8)

# f.) Exponent(**): Rasies to the power of second variable 
print(10**10)
print(2**8)

# g.) Modulus (%): This gives the remainder of the division 
print(100 % 9)
print(2 % 8)

# Hence forth operators we will discuss further.

#------------ 2.> Comparison operator : ---------------------

""" a.> '==' : This is used when we compare if two operands are equal.
             a == b

b.> '!=' : This is used when we wants true and two operands are not equal to one other.
                a!= b
c.> '<>' : This does same as not equals to operator.

d.> '>' : This is used if the value of left operand is greater than right operand.
          a > b

e.> '<' : This is used when right operand is greater than left one.
          a < b

f.> '<=' : This is used when value of right operand is equal to or less than left operand.
            a <= b

g.> '<=' : This is used when value of left operand is equal to or less than right operand.
             a >= b

#-----------------------3. Assignment Operator ------------------------------

a. > '=' : This is used to assign values to the operand or variable.
              a = 5

b.> '+=' : It adds right operand to the left operand and assign the result to left operand
            c += a is equivalent to c = c + a

c.> '-=' : It subtracts right operand to the left operand and assign the result to left operand 
          c -= a is equivalent to c = c - a

d.> '*=' : It multiplies right operand with the left operand and assign the result to left operand
            c *= a is equivalent to c = c * a

e.> '/=' : It divides right operand with the left operand and assign the result to left operand
            c /= a is equivalent to c = c / a

f.> '%=' : It modulus right operand with the left operand and assign the result to left operand
            c %= a is equivalent to c = c % a

g.> '//=' : It floor divides right operand with the left operand and assign the result to left operand
          c //= a is equivalent to c = c // a

h.> '**=' : It exponents right operand with the left operand and assign the result to left operand
          c **= a is equivalent to c = c ** a

#----------------------------------------4. Membership operatoors --------------------------------------

a.> 'in' : Evaluates to true if it finds a variable in the specified sequence and false otherwise.
           x in y, here in results in a 1 if x is a member of sequence y. 

b.> 'not in' : Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
               x not in y, here in results in a 1 if x is not a member of sequence y.

#----------------------------------------5. Identity Opeartors -------------------------------

a.> 'is' : Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
           x is y, here is results in 1 if id(x) equals id(y).

b.> 'is not' : Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.	
               x is not y, here is not results in 1 if id(x) is not equal to id(y).
