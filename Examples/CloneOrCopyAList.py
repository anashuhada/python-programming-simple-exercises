mylist = [4, 8, 2, 10, 15, 18]

# approach 1: using slicing technique
copy_mylist = mylist[:]
print(copy_mylist)

# approach 2: using extend()
copy_mylist = [10, 20, 30]
copy_mylist.extend(mylist)
print(copy_mylist)

# approach 3: using list()
copy_mylist = list(mylist)
print(copy_mylist)

# approach 4: using copy()
copy_mylist = mylist.copy()
print(copy_mylist)

# approach 5: using list comprehension
copy_mylist = [i for i in mylist]
print(copy_mylist)
