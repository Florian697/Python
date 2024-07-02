- Write a function that takes 3 arguments and prints the largest number of these arguments

def function(a, b, c):
    if a >= b:
        d = a
    else:
        d = b
    if d >= c:
        return d
    else:
        return c
l = function(1, 2, 2)
print(l)

- Make two calls to this function.
In the first call all 3 arguments are numbers
In the second call, all 3 arguments are strings

def function(a, b, c):
    d = a,b,c
    return d
l = function(1,5,7)
k = function('asdfasd','asdasd','asdasd')
print (l)
print (k)

- Write a function that takes a list of elements as an argument. We need to get the largest element from this list

def large(numbers):
    num_str = 0
    for number in numbers:
        num_str += number
    return num_str
list_1 = [12,3,7]
result = large(list_1)
print(result)

- Write a function that takes a list and adds all the values ​​from the list and returns the result.
Call a function and store the result in a variable. Print the value of a variable

def large(numbers):
    num_str = 0
    for number in numbers:
        num_str += number
    return num_str
list_1 = [12,3,7]
result = large(list_1)
print(result)













