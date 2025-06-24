# find() finds the first occurrence of specified value
# find() returns -1 if the value is not found

word = "Welcome to Python Programming"
sub_str = "Python"

if word.find(sub_str) == -1:
    print("Not found")

else:
    print("Found")
    print(word.find(sub_str))  # 11, follow index
