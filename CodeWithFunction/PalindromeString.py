def reverse_string(ori_str):
    print("Before reversing:", ori_str)
    rev_str = ori_str[::-1]
    print("After reversing:", rev_str)

    if ori_str == rev_str:
        print("Palindrome")
    else:
        print("Not Palindrome")


def main():
    reverse_string("madam")
    reverse_string("python")


main()
