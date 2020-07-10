
flower = input()
quntity = int(input())
budjet = int(input())

if flower == 'Roses':
    q = quntity * 5
    if quntity <= 80:
        price = q
    else:
        price = q - (q * 0.10)

if flower == 'Dahlias':
    q = quntity * 3.80
    if quntity <= 90:
        price = q
    else:
        price = q - (q * 0.15)

if flower == 'Tulips':
    q = quntity * 2.80
    if quntity <= 80:
        price = q
    else:
        price = q - (q * 0.15)

if flower == 'Narcissus':
    q = quntity * 3
    if quntity >= 120:
        price = q
    else:
        price = q * 1.15

if flower == 'Gladiolus':
    q = quntity * 2.5
    if quntity >= 80:
        price = q
    else:
        price = q * 1.20

if budjet >= price:
    total = budjet - price
    print(f'Hey, you have a great garden with {quntity} {flower} and {total:.2f} leva left.')
else:
    total = price - budjet
    print(f'Not enough money, you need {total:.2f} leva more.')