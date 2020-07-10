n = int(input())

result = []

for _ in range(n):
    result.append(int(input()))

s = sum(result)

if any(_==s-_ for _ in result):
    for _ in result:
        if _ == s - _:
            print('Yes')
            print(f'Sum = {s - _}')
            break
else:
    print('No')
    r = max(result) - (s - max(result))
    print(f'Diff = {abs(r)}')