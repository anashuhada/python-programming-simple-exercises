def length_string(text):
    count = 0
    for i in text:
        count += 1
    print("Length of text:", count)
    return count


def main():
    text = "Welcome"
    length_string(text)


main()
