# Now today itself we are gonna talk about classes. Classes are used to provide security in a code.

# We use class function to define a class

class calculator:

# self is uded to call in the class itself    
 
    def add(self,x,y):
        z= x+y
        print("Addition is:" + " " +  str(z))

    def sub(self,x,y):
        z= x-y
        print("Subraction is:" + " " +  str(z))
 
    def mul(self,x,y):
        z= x*y
        print("Multiplication is:" + " " + str(z))

    def div(self,x,y):
        z= x/y
        print("Division is:" + " " +  str(z))


# Now we will create the object "com1" and assign it to class.

com1 = calculator()
 
# Now its just parameter passing 

calculator.add(com1,5,5)

calculator.sub(com1,5,5)

calculator.mul(com1, 5,5)

calculator.div(com1, 5,5) 
