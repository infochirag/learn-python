#========= Hello Guys welcome to the fifth day of python classes. Today we will be learning on how to take user input and statistics in python.========


#=============================================================== User Input ===================================================================

# We use input statement with parameters to take input.


name = input("Hello whats your name : ")

print("So your name is " + " " + name)



#========================================================Statistics=====================================================================

# Well if you would have studied statistics, so you might me knowing that there are three conditions in it. Mean, Median and Mode. 

# So first we need to import Statistics..


import statistics

# we will make a list of items. We shall discuss about lists later.

exlist = [5,8,9,7,19,7,2]

# for mean

x = statistics.mean(exlist)
print(x)

y = statistics.median(exlist)
print(y)

z = statistics.mode(exlist)
print(z)
