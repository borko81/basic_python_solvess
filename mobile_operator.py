data = {
    'one': {'Small': 9.98, 'Middle': 18.99, 'Large': 25.98, 'ExtraLarge': 35.99},
    'two': {'Small': 8.58, 'Middle': 17.09, 'Large': 23.59, 'ExtraLarge': 31.79}
}


contract = input()
type_of_contract = input()
internet = input()
mounth = int(input())

if internet == 'yes':
    total = data[contract][type_of_contract]
    if total <= 10:
        total += 5.5
    elif 10 < total <= 30:
        total += 4.35
    else:
        total += 3.85
    total = total * mounth
else:
    total = data[contract][type_of_contract] * mounth


if contract == 'two':
    total = total - total * 0.0375


print(f'{total:.2f} lv.')
