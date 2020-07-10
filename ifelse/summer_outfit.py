outfiit = ""
shoes = ""

degrees = int(input())
time_of_day = input()

if time_of_day == 'Morning':
    if 10 <= degrees <= 18:
        outfiit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfiit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfiit = 'T-Shirt'
        shoes = 'Sandals'

if time_of_day == 'Afternoon':
    if 10 <= degrees <= 18:
        outfiit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfiit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfiit = 'Swim Suit'
        shoes = 'Barefoot'

if time_of_day == 'Evening':
    if 10 <= degrees <= 18:
        outfiit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfiit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfiit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfiit} and {shoes}.")