# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element1(arg, a):
    find = -1
    for i, e in enumerate(arg):
        if e == a:
            find = i 
            break
        
    return find

def find_element(arq, e):
    if e in arq:
        return arq.index(e)
    else:
        return -1

#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.


def union(arr1,arr2):
    for x in arr2:
        if x not in arr1:
            arr1.append(x)
            
    return arr1;



# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]