mylist = [93, 79, 15, 23, 30]

# approach 1: temporary variable
size = len(mylist)  # 5
temp = mylist[0]  # 93
mylist[0] = mylist[size - 1]  # 4 => 30
mylist[size - 1] = temp  # mylist[4] = temp = 93

# approach 2: tuple unpacking > assigning tuple elements to variables
mylist[0], mylist[-1] = mylist[-1], mylist[0]

# approach 3: tuple packing > combining values into a tuple
get = (mylist[-1], mylist[0])
mylist[0], mylist[-1] = get

# approach 4: * operand
# middle: create a separate sub list
start, *middle, end = mylist
# print(start) # 93
# print(middle) # [79, 15, 23]
# print(end) # 30
mylist = [end, *middle, start]

# approach 5: using pop()
first = mylist.pop(0)  # 93
last = mylist.pop(-1)  # 30
mylist.insert(0, last)
mylist.append(first)

print("List after swapping:", mylist)
