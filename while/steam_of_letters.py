words = []
word = ""
secret = {'c': 0, 'n': 0, 'o': 0}

while True:
    w = input()
    if w == 'End':
        break

    if w.isalpha():
        if w in secret and secret[w] == 0:
            secret[w] += 1
        else:
            word+=w
    if all(i==1 for i in secret.values()):
        secret = {'c': 0, 'n': 0, 'o': 0}
        words.append(word)
        word = ''


print(" ".join(words))