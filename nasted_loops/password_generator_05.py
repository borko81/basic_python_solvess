n = int(input())
l = int(input())

passwords = []
# alphabetich = {
#     0: 'a',
#     1: 'b',
#     2: 'c',
#     3: 'd',
#     4: 'f',
#     5: 'e'
# }

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for a in range(97, 97+l):
            for b in range(97, 97+l):
                for ll in range(1, n + 1):
                    if ll > x and ll > y:
                        passwords.append( "".join([str(x), str(y), chr(a), chr(b), str(ll)]))


for _ in passwords:
    print(_, end=' ')

