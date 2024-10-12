
number = int(input("Number: "))
p_count = 0
for x in range(1, number + 1):
    if number % x == 0:
        p_count += 1
if p_count == 2:
    print(f"{number } is prime!")
else:
    print(F"{number } is not prime!")


numbers = [12, 34, 3, 4, 56, 78, 13, 11, 17, 37, 33]
for x in numbers:
    count = 0
    for y in range(1, x + 1):
        if x % y == 0:
            count += 1
    if count == 2:
        print(x, " ", end="")

# Average of prime number

prime_counter = 0
prime_sum = 0
number_list = [12, 34, 3, 4, 56, 78, 13, 11, 17, 37, 33]
for x in number_list:
    count = 0
    for y in range(1, x + 1):
        if x % y == 0:
            count += 1
    if count == 2:
        prime_counter += 1
        prime_sum += x
        print(x, " ", end="")
print()
prime_average = prime_sum / prime_counter
print(f"Prime average = { prime_average}")
