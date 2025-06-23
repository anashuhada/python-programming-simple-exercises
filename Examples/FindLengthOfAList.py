# approach 1
mylist = [1, 5, 8, 3]
print(mylist)  # [1, 5, 8, 3]

count = 0

for i in mylist:
    count = count + 1

print("Length of list is", count)  # Length of list is 4

# approach 2
print("Length of list using len() is", len(mylist))  # Length of list is 4
