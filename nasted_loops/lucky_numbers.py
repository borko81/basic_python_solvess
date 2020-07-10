n = int(input())


for i in range(1111, 10000):
    test = str(i)
    if str(0) in test:
        continue
    if sum(int(i) for i in test[:2]) == sum(int(i) for i in test[2:]) and \
            n % (sum(int(i) for i in test[:2])) == 0:
        print(int(test), end=' ')