"""
Да се напише програма, която проверява дали първоначално налична сума е достатъчна, за да се заплати карта за месечен достъп във фитнес.
"""

suma = float(input())
sex = input()
age = int(input())
sport = input()


discount_young = 0.8
data = {
        'm': {'Gym': 42, 'Boxing': 41, 'Yoga': 45, 'Zumba': 34, 'Dances': 51, 'Pilates': 39},
        'f': {'Gym': 35, 'Boxing': 37, 'Yoga': 42, 'Zumba': 31, 'Dances': 53, 'Pilates': 37}
}

if age <= 19:
    needed_money = data[sex][sport] * discount_young
else:
    needed_money = data[sex][sport]

if needed_money <= suma:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f'You don\'t have enough money! You need ${(needed_money-suma):.2f} more.')
