text = "Welcome"

# approach 1: using for loop
count = 0
for x in text:
    count += 1
print("Length of the text is", count)

# approach 2: using while loop and slicing
while text[count:]:  # 0:6
    count += 1
print("Length of the text is", count)

# approach 3: using built-in len()
print(len(text))

# approach 4: using join and count
random_text = "X"
print(random_text.join(text))
print(random_text.join(text).count(random_text))  # 6
print(random_text.join(text).count(random_text) + 1)  # 7
