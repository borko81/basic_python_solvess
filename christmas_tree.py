n = int(input())

for _ in range(n+1):
    print(' ' * (n-_) + '*' * (_) + ' | '  + '*' * (_) + ' ' * (n-_))