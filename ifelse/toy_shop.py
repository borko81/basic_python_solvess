price_puzle = 2.60
price_dols = 3.00
price_bears = 4.10
price_minions = 8.20
price_truck = 2.00

price = float(input())

quantity_puzle = float(input())
quantity_dols = float(input())
quantity_bears = float(input())
quantity_minions = float(input())
quantity_truck = float(input())

total = (price_puzle * quantity_puzle) + (price_dols * quantity_dols) + \
        (price_bears * quantity_bears) + (price_minions * quantity_minions) + (price_truck * quantity_truck)

toys_price = (quantity_puzle + quantity_dols + quantity_bears + quantity_minions + quantity_truck)

if toys_price >= 50:
    total -= (total * 0.25)
else:
    total = total

final_total = total - (total * 0.1)


if (final_total >= price):
    print(f'Yes! {(final_total - price):.2f} lv left.')
else:
    print(f"Not enough money! {(price - final_total):.2f} lv needed.")