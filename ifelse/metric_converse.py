number = float(input())
in_me = input()
out_me = input()

if in_me == 'mm' and out_me == 'm':
    print(f'{number / 1000:.3f}')
elif in_me == 'mm' and out_me == 'cm':
    print(f'{number / 10:.3f}')
elif in_me == 'm' and out_me == 'cm':
    print(f'{number * 100:.3f}')
elif in_me == 'm' and out_me == 'mm':
    print(f'{number * 1000:.3f}')
elif in_me == 'cm' and out_me == 'mm':
    print(f'{number * 10:.3f}')
elif in_me == 'cm' and out_me == 'm':
    print(f'{number / 100:.3f}')
else:
    pass