#Write a function that takes a list of elements as an argument.
#We need to get the largest element from this list

def large(numbers):
    num_str = 0
    for number in numbers:
        num_str += number
    return num_str
list_1 = [12,3,7]
result = large(list_1)
print(result)