#===================================== Hello Guys welcome to the fourth day of Python learning course =================================

#---------------------------------------- Today we are gonna be writing and reading on a file.-----------------------------------------

# First we will write what we want to type to file in a variable.

writeF = "Hello Friends"

# Now we will select a variable that will give file a name. If a file exists then it will write to it else it will create it.
# We will also pass two parameters as a parameter: a.> Write  b.> Append

# Write will clear the data from the previous file and write to it.
# Append will add to the previous saved file. 

saveFile = open('savedfile.txt','w')

# We will pass what we want to write.

saveFile.write(writeF)

# Now we will close the open file.
saveFile.close()

#-----------------------------------------------------Appending to a file------------------------------------------------------------

# NOTE : We will be using upper saved file only ie savedfile.


appendText = "Some text"

appendfile =open('savedfile.txt' , 'a')

# For some new line
appendfile.write('\n')

appendfile.write(appendText)

appendfile.close()


#------------------------------------------------------ Reading a file-----------------------------------------------------------------

Readme = open('savedfile.txt', 'r').read()
print(Readme)


# Or better if we want to read lines.
Readme = open('savedfile.txt', 'r').readlines()
print(Readme)


