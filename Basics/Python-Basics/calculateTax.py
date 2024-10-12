
sales = float(input("Sales: "))
discount_rate = float(input("Discount rate: "))

discount = sales * discount_rate
print(f"Discount = ${discount}")

tax_rate = float(input("Tax rate: "))
tax = sales * tax_rate
print(F"Tax = ${ tax }")

total_price = sales - tax + discount
print(F"Total price = ${ total_price}")
