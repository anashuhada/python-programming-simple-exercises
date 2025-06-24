mylist = [20, 100, 20, 1, 10]

# approach 1: sort the list in ascending order and print the first & last elements in the list
mylist.sort()
print(mylist)  # [1, 10, 20, 20, 100]
print("Smallest element is:", mylist[0])  # 1
print("Largest element is:", mylist[-1])  # 100
first_pos, last_pos = 0, -1
print(mylist[first_pos])
print(mylist[last_pos])

# approach 2: using min() and max()
print("Smallest element is:", min(mylist))
print("Largest element is:", max(mylist))

# approach 3
max = mylist[0]
min = mylist[0]

for i in range(1, len(mylist)):
    if mylist[i] > max:
        max = mylist[i]
    elif mylist[i] < min:
        min = mylist[i]

print("Max value is:", max)
print("Min value is:", min)
