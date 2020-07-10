kilometers = float(input())
day_or_night = input()

if kilometers < 20:
    if day_or_night == 'day':
        price = (kilometers * 0.79) + 0.70
    else:
        price = (kilometers * 0.90) + 0.70
elif 20 <= kilometers < 100:
    price = kilometers * 0.09
elif kilometers >= 100:
    price = kilometers * 0.06

print(f'{(price):.2f}')