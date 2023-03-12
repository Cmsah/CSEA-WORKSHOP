# Python is a dynamically typed language
# no need to declare the type of variable
# the type is determined in Runtime
n=0
print('n=',n)
n="abc"
print('n=',n)

# Multiple assignments
n,m=0,"abc"
# multiple types in a single line also allowed
n,m,z=0.124,"abc",False

# Increment
n=n+1 #good 
n+=1  #good
#n++   syntax error

#None is null (absence of value)
n=4
n=None
print("n=",n)
# Note: In python blocks are represented using indentation instead of curly braces
#If statements dont need parenthesis or curly braces
#indentation is indicatation of the statement inside the if statement
n=1
if n>2:
    n-=1
elif n==2:
     n*=2
else :
     n+=2
#parenthesis needed for the multiline conditions.
# &&->'and' in python
# ||-> 'or' in python
n,m=1,2
if((n>2 and n!=m)or(n==m)):
     n+=1

#loops

#While loops similar 
n=0
while n<5:
    print(n)

    
# for loop
# i is variable its incremented internally range(5)=>(0,5) 5 exclusive
for i in range(5):
     print(i)
# i=2
for i in range(2,5):
     print(i)
# i=1 and reverse iteration
for i in range(5,1,-1):
     print(i) 

# basically range(stop) range(start,stop,step)
# step => interval 
# by defult start is 0 and step is 1
# for in , for in enumerate for in zip covered in arrays lesson


# Math Operation

# 1>Division
# / => decimal division by default
print(5/2)#2.5
# //=> rounds down to give int 
print(5//2)#2
# note: most languages round towards zero by default but python will round down
# i.e -3/2 = -1 in c++
print(-3//2)#-2
# Work around is use decimal division and convert ans to integer
print(int(-3/2))#-1

# 2>Mod operator
# for positive nos it works as expected
print(10%3)#1
# for negative values
# in background this is how mod is implemented
# a%b = a — math.floor(a/b)*base
# -10-floor(-10/3)*3=-10+4*3=2
print(-10%3)#2

# to get requried mod behaviour
import math
print(math.fmod(-10,3))//-1

# 3>Useful math helpers
print(math.floor(3/2))#1
print(math.ceil(3/2))#2
print(math.sqrt(2))#1.41
print(math.pow(2,3))#8

#4> max/min int
# python nos is infinite and never overflow
# INT_MAX
float("inf")
# INT_MIN
float("-inf")






