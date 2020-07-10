a = int(input())
b = int(input())

result = []

for i in range(a, b + 1):
    for k in range(a, b + 1):
        for y in range(a, b + 1):
            for z in range(a, b + 1):
                if i % 2 == 0 and z % 2 == 1 and i > z and (k + y) % 2 == 0 :
                    print(f"{i}{k}{y}{z}", end=' ')
                elif i % 2 == 1 and z % 2 == 0 and i > z and (k + y) % 2 == 0:
                    print(f"{i}{k}{y}{z}", end=' ')