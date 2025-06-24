mylist = [1, 6, 3, 5, 3, 4]

# approach 1: using loop
ele = 2
flag = 0

for i in mylist:
    if i == ele:
        print("Element found")
        flag = 1
        break
if flag == 0:
    print("Element not found")

# approach 2: using in operator
ele = 100

if ele in mylist:
    print("Element found")
else:
    print("Element not found")
