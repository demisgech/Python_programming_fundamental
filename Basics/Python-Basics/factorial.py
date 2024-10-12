
fact = 1
number = int(input("Number: "))
if number < 0:
    print("Sorry, number should be positive!")
else:
    if number == 1 or number == 0:
        pass
    else:
        for x in range(1, number + 1):
            fact *= x
    print(F"{ number }! = {fact}")