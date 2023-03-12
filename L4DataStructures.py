# 1>Stack 
# For stack use lists itself

# 2>Queue
# double ended queues by default
# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
# deque([1, 2])

# since it is double ended can be popped from left side
queue.popleft()
print(queue)
# deque([2])

# appendin to left side
queue.appendleft(1)
print(queue)
# deque([1, 2])

queue.pop()
print(queue)
# deque([1])

# 3>Set
# Can be search, insert and remove elements in O(1) time
# there cant be any duplicates in Set
# lenght gives no of elements in Set

mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(1)
print(mySet)
# {1, 2}

print(len(mySet))
# 2

# Use in operator to search the Set
print(1 in mySet)
# True
print(2 in mySet)
# True
print(3 in mySet)
# False

mySet.remove(2)
print(2 in mySet)
# False

# initialise list to set
print(set([1, 2, 3]))
# {1, 2, 3}

# Set comprehension
mySet = { i for i in range(5) }
print(mySet)
# {0, 1, 2, 3, 4}

# 4>HashMap i.e dictionary
# Stores unique value pairs
# i.e no duplicate keys
# similar to lists use curly braces for hashmap/dictionary

myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
# {"alice": 88, "bob": 77}

# len gives no of keys in hashmap
print(len(myMap))
# 2

# value mapped to key can be modifeid
myMap["alice"] = 80
print(myMap["alice"])
# 80

print("alice" in myMap)
# True

# removal of key also removes value
myMap.pop("alice")
print("alice" in myMap)
# False

myMap = { "alice": 90, "bob": 70 }
print(myMap)
#   key:value
# { "alice": 90, "bob": 70 }

# Dictionary comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)
# { 0: 0, 1: 2, 2: 4 }

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])
# "alice" 90
# "bob" 70

# Looping Without key
for val in myMap.values():
    print(val)
# 90
# 70

# Using unpacking
for key, val in myMap.items():
    print(key, val)
# "alice" 90
# "bob" 70

# 5>Tuples

# Tuples are like lists but immutable
# use parenthesis instead of square bracket

tup = (1, 2, 3)
print(tup)
# (1, 2, 3)


print(tup[0])
# 1

print(tup[-1])
# 3

# Can't modify, this won't work
tup[0] = 0

# mainly tuples are used as keys for hashmap or hashset
# mapping a pair of values to 3
myMap = { (1,2): 3 }
print(myMap[(1,2)])
# 3

# lists are not accepted as keys so have to use tuples instead
myMap[[3, 4]] = 5

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)
# True


# 6>Heaps

import heapq

# under the hood heaps are arrays
# by default heaps in python is min heap
minHeap = []

heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])
# 2


while len(minHeap):
    print(heapq.heappop(minHeap))
# 2 3 4

# No max heaps by default, work around is
# to use min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])
# 4

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
# 4 3 2


# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))
# 1 2 4 5 8
