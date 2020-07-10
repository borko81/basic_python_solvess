town = 'Sofia Varna Plovdiv'.split(' ')

t = input()
quanity = float(input())

if t not in town:
    print('error')
elif t == 'Sofia' and 0 <= quanity <= 500:
    print(f'{(quanity * 0.05):.2f}')
elif t == 'Sofia' and 500 <= quanity <= 1000:
    print(f'{(quanity * 0.07):.2f}')
elif t == 'Sofia' and 1000 <= quanity <= 10000:
    print(f'{(quanity * 0.08):.2f}')
elif t == 'Sofia' and quanity > 10000:
    print(f'{(quanity * 0.12):.2f}')
elif t == 'Varna' and 0 <= quanity <= 500:
    print(f'{(quanity * 0.045):.2f}')
elif t == 'Varna' and 500 <= quanity <= 1000:
    print(f'{(quanity * 0.075):.2f}')
elif t == 'Varna' and 1000 <= quanity <= 10000:
    print(f'{(quanity * 0.10):.2f}')
elif t == 'Varna' and quanity > 10000:
    print(f'{(quanity * 0.13):.2f}')
elif t == 'Plovdiv' and 0 <= quanity <= 500:
    print(f'{(quanity * 0.055):.2f}')
elif t == 'Plovdiv' and 500 <= quanity <= 1000:
    print(f'{(quanity * 0.08):.2f}')
elif t == 'Plovdiv' and 1000 <= quanity <= 10000:
    print(f'{(quanity * 0.12):.2f}')
elif t == 'Plovdiv' and quanity > 10000:
    print(f'{(quanity * 0.145):.2f}')
else:
    print('error')