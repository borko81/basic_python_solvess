from math import floor, ceil

quantity_magnolii = int(input())
quantity_zumbule = int(input())
quantity_rose = int(input())
quantity_kaktus = int(input())
price_gift = float(input())

price_otder = quantity_magnolii * 3.25 + quantity_zumbule * 4 \
    + quantity_rose * 3.50 + quantity_kaktus * 8

dutty = price_otder - price_otder * 0.05

if dutty < price_gift:
    print(f'She will have to borrow {ceil(price_gift - dutty)} leva.')
else:
    print(f'She is left with {floor(dutty - price_gift)} leva.')