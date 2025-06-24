# reverse a text
text = "hello"
rev_text = text[::-1]
print(rev_text)

# reverse a sentence
word = "Welcome to Python Programming"
# words = str.split(" ") # ['Welcome', 'to', 'Python', 'Programming']
# print(words)
# words = words[::-1]
# print(words)
# output = ' '.join(words)
# print(output)

combine_word = ' '.join(word.split(" ")[::-1])  # Programming Python to Welcome
print(combine_word)
