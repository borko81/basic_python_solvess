"""
За великденските празници, магазин започва да продава три вида великденска
украса – кошнички за яйца (basket), великденски венци (wreath) и шоколадови зайци
(chocolate bunny). Вашата задача е да напишете програма, която да изчислява каква сметка
трябва да плати всеки един клиент на магазина, като се има в предвид, че всеки клиент
закупил четен брой продукти, ще получи 20% отстъпка от крайната цена.
След като всички клиенти приключат с покупките, трябва да се отпечата средно по колко пари
е похарчил всеки човек.
Цените на продуктите са:
    • кошничка за яйца (basket) – 1.50 лв.
    • великденски венец (wreath) – 3.80 лв.
    • шоколадов заек (chocolate bunny) – 7 лв.
"""

clients = int(input())
total_sum = []


while clients > 0:
    client_order = 0
    count_order = 0
    into = 0
    while True:
        shop = input()
        if shop == 'Finish':
            if into % 2 == 0:
                client_order = client_order - client_order * 0.2
            print(f'You purchased {count_order} items for {(client_order):.2f} leva.')
            total_sum.append(client_order)
            break
        if shop == 'basket':
            client_order += 1.5
            count_order += 1
            into += 1
        elif shop == 'wreath':
            client_order += 3.8
            count_order += 1
            into += 1
        elif shop == 'chocolate bunny':
            client_order += 7
            count_order += 1
            into += 1
    clients -= 1


print(f'Average bill per client is: {(sum(total_sum) / len(total_sum)):.2f} leva.')