mylist = [6, 0, 4, 1]

# approach 1: using clear()
print("My list before clearing:", mylist) # [6, 0, 4, 1]
mylist.clear()
print("My list after clearing:", mylist) # []

# approach 2: initialize the list with no value
print("My list before clearing:", mylist)  # [6, 0, 4, 1]
mylist = []
print("My list after clearing:", mylist)  # []

# approach 3: using *=0
print("My list before clearing:", mylist)  # [6, 0, 4, 1]
mylist *= 0
print("My list after clearing:", mylist)  # []

# approach 4: using del
print("My list before clearing:", mylist)
# del mylist[1:3] #  [6, 1]
del mylist[:]  # []
print("My list after clearing:", mylist)
