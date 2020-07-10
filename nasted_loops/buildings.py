floor = int(input())
rooms = int(input())

for f in range(floor, 0 ,-1):
    if f == floor:
        print(" ".join([f'L{f}{r}' for r in range(rooms)]))
    if f % 2 == 1 and f != floor:
        print(" ".join([f'A{f}{r}' for r in range(rooms)]))
    elif f % 2 == 0 and f != floor:
        print(" ".join([f'O{f}{r}' for r in range(rooms)]))