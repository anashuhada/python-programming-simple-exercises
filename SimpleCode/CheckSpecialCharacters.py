import re

word1 = "Welcome@@2to%%Python**Programming@!!^%%@$"
word2 = "Welcome to Python Programming"
regex = re.compile('[~!@#$%^&*()_+{}<>?`|;/.,]')

if regex.search(word2) is None:
    print("No special characters present in a string")
else:
    print("String contains special characters")
