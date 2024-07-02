#Write a function that takes 3 arguments and prints the largest number of these arguments

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