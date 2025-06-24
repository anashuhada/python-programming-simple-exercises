mylist = [10, 20, 4, 45, 99]

# approach 1
mylist.sort()
print(mylist)  # [4, 10, 20, 45, 99]
print("Largest number is:", mylist[-1])
print("Largest number is:", mylist[-2])

# approach 2
new_mylist = set(mylist)
# print(new_mylist) # {99, 4, 10, 45, 20}
print(max(new_mylist))  # 99
new_mylist.remove(max(new_mylist))
print(max(new_mylist))  # 45
