"""
1
2 3
4 5 6
7
"""


n = int(input())
c = 1

for x in range(1, n + 1):
    for y in range(1, x + 1):
        if c == n + 1:
            break
        print(c, end=' ')
        c += 1
    print()