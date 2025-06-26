def reverse_a_string(text):
    print("Before reversing:", text)
    rev = text[::-1]
    print("After reversing:", rev)
    return rev


def reverse_a_sentence(word):
    print("Before reversing:", word)
    rev = ' '.join(word.split(' ')[::-1])
    print("After reversing:", rev)
    return rev


def main():
    text = "Python"
    word = "Welcome to Python Programming"
    reverse_a_string(text)
    reverse_a_sentence(word)


main()
