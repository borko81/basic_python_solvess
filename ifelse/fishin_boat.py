budjet = int(input())
season = input()
quntity = int(input())


if season == 'Spring':
    ship_price = 3000
elif season == 'Summer' or season == 'Autumn':
    ship_price = 4200
else:
    ship_price = 2600

if quntity <= 6:
    ship_price = ship_price - (ship_price * 0.1)
elif quntity <= 11:
    ship_price = ship_price - (ship_price * 0.15)
else:
    ship_price = ship_price - (ship_price * 0.25)

if quntity % 2 == 0 and season != 'Autumn':
    ship_price = ship_price - (ship_price * 0.05)

if budjet < ship_price:
    left = ship_price - budjet
    print(f"Not enough money! You need {left:.2f} leva.")
else:
    income = budjet - ship_price
    print(f"Yes! You have {income:.2f} leva left.")