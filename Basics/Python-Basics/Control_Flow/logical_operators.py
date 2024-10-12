# Logical Operators
# Logical AND(and)
# If it is True, both operand must be True
print("---- Logical AND ----")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Logical OR(or)
# If it is True, at least one operand must be True
print("---- Logical Or ----")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Logical NOT(not)
# It produces the reverse of the value whatever we had before
print("---- Logical NOT ----")
print(not True)
print(not False)

# More on logical Operators
# Logical AND(and)
print("Logical and")
print(True and 10)  # 10
print(False and 10)  # False
print(0 and False)  # 0
print(12 and 13)  # 13
print(12 and 0)  # 0
print(0 and 12)  # 0
print(1 and "Demis")  # Demis
print(0 and "Demis")  # 0
print("Alex" and "Demis")  # Demis

# Logical or
print("Logical or")
print(True or 10)  # True
print(False or 10)  # 10
print(0 or False)  # 0
print(12 or 13)  # 12
print(12 or 0)  # 12
print(0 or 12)  # 12
print(1 or "Demis")  # 1
print(0 or "Demis")  # Demis
print("Alex" or "Demis")  # Alex

# Logical not
print("Logical not")
print(not False)  # True
print(not 12)  # False
print(not "Demis")  # False
print(not "")  # True
