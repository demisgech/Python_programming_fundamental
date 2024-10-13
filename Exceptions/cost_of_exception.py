from timeit import timeit

code1  = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass
"""

code2  = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
excution_time = timeit(code1,number=10000)
print("First code",excution_time)

excution_time = timeit(code2,number=10000)
print("Second code",excution_time)