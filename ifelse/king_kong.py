import sys

budjet = float(input())

if 1.00 > budjet > 1000000.00:
    sys.exit()

peoples = int(input())

if 1 > peoples > 500:
    sys.exit()

price_static_clotes = float(input())

if 1.00 > price_static_clotes > 1000.00:
    sys.exit()

amount_decor = budjet * 0.1

if peoples >= 150:
    discount = (peoples * price_static_clotes) / 10
    amount_of_clotes = (peoples * price_static_clotes) - discount
else:
    amount_of_clotes = peoples * price_static_clotes

total_movie = amount_decor + amount_of_clotes

total_movie_left_money = budjet - total_movie

if total_movie_left_money >= 0:
    print("Action!")
    print(f'Wingard starts filming with {total_movie_left_money:.2f} leva left.')
else:
    print("Not enough money!")
    print(f'Wingard needs {abs(budjet - total_movie):.2f} leva more.')