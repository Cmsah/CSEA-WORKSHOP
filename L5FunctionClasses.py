
# Function

def myFunc(n, m):
    return n * m

print(myFunc(3, 4))
# 12

# Nested functions have access to outer variables
# Useful for recursion
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))
# "abc"

# Can modify objects but not reassign values
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        
        # will only modify val in the helper scope
        # val *= 2
    
        # val*=2 o/p will be 3 itself
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)
# [2, 4] 6

# Lambda Function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression

x = lambda a : a + 10
print(x(5))

y= lambda a, b, c : a + b + c
print(y(5, 6, 2))


# Classes

class MyClass:
    # Constructor
    # self is same as this 
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)
    
    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

myObj = MyClass([1, 2, 3])
print(myObj.getLength())
# 3
print(myObj.getDoubleLength())
# 6