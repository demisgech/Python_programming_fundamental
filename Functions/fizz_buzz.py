def fizz_buuzz(input):

    if input % 5 == 0 and input % 3 == 0:
        return "Fizz buzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return str(input)

print(fizz_buuzz(45))