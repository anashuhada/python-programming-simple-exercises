mylist = [5, 10, 15, 50]

# approach 1: using for loop with range()
total = 0

for i in range(0, len(mylist)):
    total = total + mylist[i]

print("Sum of all elements in given list:", total)

# approach 2: using sum()
print("Sum of all elements in given list:", sum(mylist))

# approach 3: using normal for loop
total = 0
for i in mylist:
    total += i

print("Sum of all elements in given list:", total)
