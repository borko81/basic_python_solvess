budjet = float(input())
season = input()

if budjet <= 100:
    town = 'Bulgaria'
    if season == 'summer':
        left = budjet * 0.3
        camp = 'Camp'
    else:
        left = budjet * 0.7
        camp = 'Hotel'

elif budjet <= 1000:
    town = 'Balkans'
    if season == 'summer':
        left = budjet * 0.4
        camp = 'Camp'
    else:
        left = budjet * 0.8
        camp = 'Hotel'

elif budjet > 1001:
    town = 'Europe'
    left = budjet * 0.9
    camp = 'Hotel'

print(f'Somewhere in {town}')
print(f'{camp} - {left:.2f}')