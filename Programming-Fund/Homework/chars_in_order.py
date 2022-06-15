def asciiboyz(char1, char2):
    text = []
    for x in range(ord(char1) + 1, ord(char2)):
        text.append(chr(x))
    return ' '.join(text)


print(asciiboyz(input(), input()))
