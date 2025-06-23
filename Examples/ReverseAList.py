mylist = [10, 11, 12, 13, 14, 15]

# approach 1: using reverse()
print("Before reversing:", mylist)  # [10, 11, 12, 13, 14, 15]
mylist.reverse()
print("After reversing:", mylist)  # [15, 14, 13, 12, 11, 10]

# approach 2: using slicing technique
print("Before reversing:", mylist)  # [10, 11, 12, 13, 14, 15]
new_mylist = mylist[::-1]
print("After reversing:", new_mylist)  # [15, 14, 13, 12, 11, 10]
