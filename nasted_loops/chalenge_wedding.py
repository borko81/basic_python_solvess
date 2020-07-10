men = int(input())
women = int(input())
tables = int(input())

for m in range(1, men + 1):
    for w in range(1, women + 1):
        print(f'({m} <-> {w})', end=' ')
        tables -= 1
        if tables == 0:
            break
    if tables == 0:
        break
