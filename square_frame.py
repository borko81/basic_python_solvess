n = int(input())

print('+ ' + '- '* (n - 2) + '+')
for r in range(n-2):
    print('| ' + '- ' * (n-2) + '|', end='')
    print()
print('+ ' + '- '* (n - 2) + '+')