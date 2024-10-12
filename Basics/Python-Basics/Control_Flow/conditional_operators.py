x = 100
y = 20
# This conditional(Ternary) operators(?:) (in other languages) replaced by the following code in python
# Other languages such as: js,ts,c,c++,c#,java uses
#  result = x > y ? "Greater" : "less"
result = "Greater" if x > y else "Less"
print(result)

age = 15
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

number = int(input("Number: "))
even_or_odd = "Even" if number % 2 == 0 else "Odd"
print(even_or_odd)