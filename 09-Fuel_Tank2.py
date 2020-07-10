gasoline = 2.22
diesel = 2.33
gas = 0.93

gasoline_card_diskount = 0.18
diesel_card_diskount = 0.12
gas_card_diskount = 0.08

fuel_choice = input()
fuel_quanity = float(input())
has_card = input()

if fuel_choice == 'Gas':
    price = fuel_quanity * gas
    if has_card == 'Yes':
        price = price - fuel_quanity * gas_card_diskount
elif fuel_choice == 'Gasoline':
    price = fuel_quanity * gasoline
    if has_card == 'Yes':
        price = price - fuel_quanity * gasoline_card_diskount
else:
    price = fuel_quanity * diesel
    if has_card == 'Yes':
        price = price - fuel_quanity * diesel_card_diskount

if 20 < fuel_quanity <= 25:
    price = price - price * 0.08
elif fuel_quanity > 25:
    price = price - price * 0.1


print(f'{price:.2f} lv.')