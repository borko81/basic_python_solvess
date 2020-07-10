a = ord(input())
c = ord(input())
b = ord(input())

result = []

for i in range(a, c+1):
    for k in range(a, c+1):
        for z in range(a, c+1):
            word = chr(i) + chr(k) + chr(z)
            if chr(b) not in word:
                result.append(word)

print(" ".join(result), len(result))