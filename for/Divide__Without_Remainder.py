n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    _ = int(input())
    if _ % 2 == 0:
        p1 += 1
    if _ % 3 == 0:
        p2 += 1
    if _ % 4 == 0:
        p3 += 1


print(f'{(p1 / n*100):.2f}%')
print(f'{(p2 / n*100):.2f}%')
print(f'{(p3 / n*100):.2f}%')