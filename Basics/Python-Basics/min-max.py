
numbers = [12, 34, 56, 78, 12, 34, 100, -100]
minNumber = numbers[0]
for number in numbers:
    if minNumber > number:
        minNumber = number
print(f"Minimum Number = {minNumber}")

maxNumber = numbers[0]
for number in numbers:
    if maxNumber < number:
        maxNumber = number
print(f"Maximum Number = {maxNumber}")
