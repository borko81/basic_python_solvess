budjet = float(input())

equip_order = 0
count = 0
total_price = 0

while True:
    equipment = input()
    if equipment == 'Stop':
        print(f'You bought {equip_order} products for {total_price:.2f} leva.')
        break
    count += 1
    price = float(input())
    if count % 3 == 0:
        price /= 2
    if price > budjet:
        print(f'You don\'t have enough money!')
        print(f'You need {(price - budjet):.2f} leva!')
        break
    else:
        equip_order += 1
        total_price += price
        budjet -= price



