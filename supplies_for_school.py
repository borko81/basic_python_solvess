pencil = int(input())
marker = int(input())
preparad = float(input())
discount = int(input())

total_price_without_discount = (pencil * 5.8) + (marker * 7.2) + (preparad * 1.2)

with_disount = total_price_without_discount - ((total_price_without_discount * discount) / 100)

print(f'{with_disount:.3f}')