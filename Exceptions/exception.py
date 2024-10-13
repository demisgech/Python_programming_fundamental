# An exception is a kind of error that terminate the excution of the program

numbers = [1,2,3]
#print(numbers[3]) # throw an exeption

# Handling exeption
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown")
# print("Excution continues.")

try:
    age = int(input("Age: "))
except ValueError as exception:
    print("You did't enter a valid age.")
    print(exception)
    print(type(exception))