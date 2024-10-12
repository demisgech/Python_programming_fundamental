
course = "  Python programming"
print(course.capitalize())

print(course.upper())
print(course.lower())
print(course.count('o',None))
print(course.title())

# Removing a space from the beginning and end
print(course.strip())
print(course.lstrip())
print(course.rstrip())

print(course.isalpha())  # False, cause it contains a space

course = "Python"
print(course.isalpha())  # True

course = "Python programming"
print(course.expandtabs(10))
print(course.rsplit(' ',10))
print(course.find('Pyth'))  # return index of a character

print(course.replace("P", "J"))

print("pro" in course)  # return boolean (True or False)

print("Swift" not in course)