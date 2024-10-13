try:
    age = int(input("Age: "))
    xfactor = 10/age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
else:
    print("No exception were thrown.")

# throwing multiple exception in one line
try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown.")