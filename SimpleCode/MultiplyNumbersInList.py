mylist = [3, 2, 4]

# approach 1: traversal
res = 1

for x in mylist:
    res = res * x

print("Result:", res) # Result: 24

# approach 2: using numpy.prod() - install numpy package
import numpy

result = numpy.prod(mylist)
print("Result:", result) # Result: 24
