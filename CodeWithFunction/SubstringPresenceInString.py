def find_string(word, sub_str):
    if word.find(sub_str) == -1:
        print("Not found")

    else:
        print("Found")
        print(word.find(sub_str))


def main():
    find_string("Welcome to Python Programming", "Python")


main()
