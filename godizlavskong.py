budjet = float(input())
statists = int(input())
price_clotes_for_statis = float(input())

decor = budjet * 0.1

if statists > 150:
    price_clotes_for_statis = price_clotes_for_statis - price_clotes_for_statis * 0.1
    total_price_for_clots = statists * price_clotes_for_statis
else:
    total_price_for_clots = statists * price_clotes_for_statis

total_price = decor + total_price_for_clots

if total_price <= budjet:
    print('Action!')
    print(f'Wingard starts filming with {(budjet-total_price):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(budjet - total_price):.2f} leva more.')
