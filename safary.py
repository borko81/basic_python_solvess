price_diesel = 2.1
guide = 100
discont_satyrday = 0.1
discount_sunday = 0.2

budjet = float(input())
fuel = float(input())
day = input()

total = (fuel * price_diesel) + guide
if day == 'Saturday':
    total = total - total * discont_satyrday
else:
    total = total - total * discount_sunday


if total <= budjet:
    print(f'Safari time! Money left: {(budjet - total):.2f} lv. ')
else:
    print(f'Not enough money! Money needed: {(total - budjet):.2f} lv.')
