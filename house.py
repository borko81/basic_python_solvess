n = int(input())

if n % 2 == 1:
    for _ in range((n + 1) // 2):
        l = '*' * (_ * 2 + 1)
        print(l.center(n, '-'))
else:
    for _ in range((n + 1) // 2):
        l = '**' * (_ + 1)
        print(l.center(n, '-'))
for _ in range(n//2):
    l = '*'
    print('|' + l.center(n - 2, '*') + '|')