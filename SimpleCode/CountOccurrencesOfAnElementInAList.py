mylist = [15, 6, 7, 10, 12, 20, 10, 28, 10]

# approach 1: using loop
x = 10
count = 0
for i in mylist:
    if i == x:
        count = count + 1
print("{} has occurred {} times".format(x, count))  # print(x, "has occurred", count, "times")

# approach 2: using count()
x = 10
print("{} has occurred {} times".format(x, mylist.count(x)))

# approach 3: using counter()
from collections import Counter

x = 10
dict = Counter(mylist)
# print(dict) # {10: 3, 15: 1, 6: 1, 7: 1, 12: 1, 20: 1, 28: 1}
print("{} has occurred {} times".format(x, dict[x]))
