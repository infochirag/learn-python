# Lets talk about Exception Handling today.

""" We use two things in Exception Handling : Try and except.
Well try throws an error that is syntactically wrong. like division by zero. This would run but not throw an error and we know division by zero is wrong.

Except block catches the error thrown by try block.
"""

try:
    print("Running the try...")
    print("5" + 5)

# Now we know that this is wrong so we will try to solve this error in except block.

except TypeError as t:
    print("Type Error Triggered")


except NameError as n:
    print("Name Error Triggered")

# Now we knew that adding string to variable was an error so we triggered it.
