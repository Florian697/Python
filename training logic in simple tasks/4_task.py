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