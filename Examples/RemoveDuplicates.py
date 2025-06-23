mylist = ["geeks", "for", "geeks", "geeks"]
mylist = list(dict.fromkeys(mylist))
print(mylist)  # ['geeks', 'for']

mynumber = [20, 55, 96, 61, 33, 52, 55, 20]
# mynumber = list(dict.fromkeys(mynumber))
# print(mynumber) # [20, 55, 96, 61, 33, 52]

duplicates = []

for i in mynumber:
    if mynumber.count(i) > 1 and i not in duplicates:
        # print("Duplicates found", i)
        duplicates.append(i)
print("Duplicates found", duplicates)
