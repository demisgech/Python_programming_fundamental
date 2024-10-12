
# def greet():
#     print("Hi there!")
#     print("Welcome abroad")

# def greet(name):
#     print(f"Hello {name}")
# greet("Demis")

def greet(title, name) -> None:
    print(f"Hello {title} {name}")

# greet("Mr.","Demis")
# greet("Professor","Demis")

# Functions
# 1- Performing a task
# 2- Return a value

def get_greeting(name):
    return name


message = get_greeting("Demis")
print(message)

file = open("content.txt","w")
file.write(message)

file = open("content.txt","w")
file.write(message)

