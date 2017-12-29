# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(arr):
    # Your code here

    if not arr:
        return True
    else:
        l = len(arr)
        c = len(arr[0])

    if l != c:
        return False
    else:
        y = 0
        x = 0
    
    x = 0
    while x < l:
        y = 0
        while y < l:
            if arr[x][y] != arr[y][x]:
                return False
            y += 1
        x += 1
    
    return True


print symmetric([[1, 2, 3],[2, 3, 4], [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False