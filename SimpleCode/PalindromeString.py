# approach 1
# reverse a string
# check if reversed and original are same or not

ori_str = input("Enter a string: ")  # abcdef
# print(ori_str[:])  # abcdef
# print(ori_str[0:5])  # abcde
# print(ori_str[0:5:1])  # abcde
# print(ori_str[::]) # abcdef
# print(ori_str[::-1]) # reverse

rev_str = ori_str[::-1]

if ori_str == rev_str:
    print("Palindrome")
else:
    print("Not palindrome")
