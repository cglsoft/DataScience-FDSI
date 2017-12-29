# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def max(a,b,c):
    if (a>b):
        if(a>c):
            max = a 
        else:
            max = c
    else:
        if (b>c):
            max = b
        else:
            max = c
    return max

def min(a,b,c):
    if (a<b):
        if(a<c):
            min = a 
        else:
            min = c
    else:
        if (b<c):
            min = b
        else:
            min = c
    return min

def set_range(a,b,c):
    return  max(a,b,c)-min(a,b,c)
    
        
print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6