# Relearn comprehesion part
# https://stackoverflow.com/questions/15654800/what-is-the-difference-between-0-for-in-range10-for-in-range10-and

# Arrays are called lists in python
# dynamic by default so can be used as stack using append() and pop()

arr=[1,2,3]
print(arr)#[1, 2, 3]
arr.append(4)
arr.append(5)
print(arr)#[1, 2, 3, 4, 5]
arr.pop()
print(arr)#[1, 2, 3, 4]

# inserting in middle
#         (index,value)
arr.insert(1,7)#O(n) operation

# indexing same as cpp indexing in o(1) operation
arr[0]=0

# ARRAY INITIALIZATOIN
# len(arr) gives the length of array
# to initialize a array of variable size n with default value 1
n=5
arr=[1]*n
print(arr)

# negative index in  py means reading from the end of array
# -1 gives last value
print(arr[-1],arr[-2])

# 1>Subarray (slicing)
arr=[1,2,3,4,5]

#  start index is inclusive and end index is exclusive
#  default start is 0th inclusive defualt end is arraysize+1
#  [start:end:step]
subarr=arr[1:3]#[2,3]
print(subarr)
# Use the minus operator to refer to an index from the end:
print(arr[-2:1:-1])#[4, 3]

# 2> Array Unpacking
a,b,c=[1,2,3]#a=1,b=2,c=3
print(a,b,c)#1 2 3
# note: No. of var on lhs should match no. of elements on rhs

# 3>Looping through arrays

# Using index
for i in range(len(arr)):
    print(arr[i])

# Without index
nums=arr
# num is a variable
for num in nums:
    print(num)

# Using both index and value
# unpacking index and value in i and n
for i,num in enumerate(nums):
    print(i,n)

# simultaneously looping thru two arrays simultanously with unpacking
nums1=[1,2,3]
nums2=[2,4,6]
# zip takes both arrays and combines them to make a array of pair
# and unpack pair of values 

for n1,n2 in zip(nums1,nums2):
    print(n1,n2)

# 3>Reversing the array
nums.reverse()
print(nums)#5 4 3 2 1

# 4>Sorting the array
arr=[5,4,7,3,8]
arr.sort()
# by default sorts in ascending order
print(arr)# [5,4,7,3,8]
# for descending order 
arr.sort(reverse=True)# [8,3,7,4,5]

# for string array by default it returns in alphabetical order
# for custorm sorting behaviour we pass comparator funcition as parameter called key
# and pass lambda function or normal function
# e.g sort array in length of x
str=['bob','alice','jane','doe']
# key passed is gonna be used to sort the string
# take each value of x from the array and return the length of string
str.sort(key=lambda x:len(x))
print(str)# ['bob', 'doe', 'jane', 'alice']
# or
def cmp(x):
    return len(x)
         
str.sort(key=cmp)
print(str)# ['bob', 'doe', 'jane', 'alice']

# 5> List Comprehension
nums=[i for i in range(5)]
print(nums)# [0,1,2,3,4]

# 2d list
# https://stackoverflow.com/questions/15654800/what-is-the-difference-between-0-for-in-range10-for-in-range10-and
arr=[[0]*4 for i in range(4)]
# 4x4 grid of all zero
print(arr)# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(arr[0][0],arr[3][3])
# note: this is copying a reference to the same object, ten times It is equivalent to
arr=[[0]*4]*4
print(arr)
print(arr[0][0],arr[3][3])








