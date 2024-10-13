
try:
    file = open("exception.py")
    age = int(input("Age: "))
    xfactor = 10/age
    file.close() # Not recommended, 
    # if exception thrown in one of the above two line file will not be closed
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
    file.close() # Not recommended, unless exception thrown file will not be closed
else:
    print("No exception were thrown.")
    file.close() # Not recommended  if multiple exception thrown code will be duplicated

# The best way
try:
    file = open("exception.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")
finally:
    file.close()

# The more elegant way
try:
    with open("exception.py") as file:
        print("File opend.")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")

try:
    with open("exception.py") as file, open("another.py") as another:
        print("File opend.")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")