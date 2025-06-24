mylist = [23, 65, 19, 90]

# approach 1: simple swap
print(mylist)
pos1, pos2 = 1, 3  # first and third position
mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]

# approach 2: using built-in list.pop()
pos1, pos2 = 1, 3
first_element = mylist.pop(pos1)  # 65
second_element = mylist.pop(pos2 - 1)  # 23, 19, 90
mylist.insert(pos1, second_element)
mylist.insert(pos2, first_element)

# approach 3: using tuple
pos1, pos2 = 1, 3
get = (mylist[pos1], mylist[pos2])
mylist[pos2], mylist[pos1] = get
print(mylist)
