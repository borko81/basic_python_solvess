n1 = int(input())
n2 = int(input())
n3 = int(input())

for i in range(2, n1 + 1, 2):
    for k in range(2, n2 + 1):
        for z in range(2, n3 + 1, 2):
            for t in range(2, k):
                if k % t == 0:
                    break
            else:
                print(i, k, z)