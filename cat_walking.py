minuti_raz = int(input())
min_raz = int(input())
cal = int(input())

razhod = (minuti_raz * min_raz) * 5

if razhod >= cal // 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {razhod}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {razhod}.')

