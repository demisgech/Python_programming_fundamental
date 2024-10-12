from array import array

# array(typecode,iterable)
numbers = array('i',[1,2,3,4])
numbers.append(6)
numbers.pop()
print(numbers[0])

numbers[1] = 1.0 # typecode error
# 'float' object connot be interpreted as iinteger
