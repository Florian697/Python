#Make two calls to this function.
#In the first call all 3 arguments are numbers
#In the second call, all 3 arguments are strings

def function(a, b, c):
    d = a,b,c
    return d
l = function(1,5,7)
k = function('asdfasd','asdasd','asdasd')
print (l)
print (k)