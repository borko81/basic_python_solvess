number = int(input())

for _ in range(1111, 9999 + 1):
    a = _ // 1000
    b = (_ // 100) % 10
    c = (_ // 10) % 10
    d = (_ % 10)
    if a == 0 or b == 0 or c == 0 or d == 0:
        continue
    else:
        if number % a == 0 and number % b == 0 and number % c == 0 and number % d == 0:
            print(_, end=' ')