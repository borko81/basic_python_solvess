"""
Сезона за изкачване на алпийски върхове започва и всички алпинисти, се запасяват с енергийни гелове за изкачването. Фирма предлага малки и големи разфасовки с по 2 бр. и 5 бр. енергийни гела, като цената на един гел зависи от плодовете, от които е направен. В зависимост от размера на разфасовката, цената за брой енергиен гел е различна. От конзолата се четат плодовете, размерът на опаковката ((малка) 2 бр. или (голяма) 5 бр.), както и колко разфасовки са поръчани. Да се напише програма, която изчислява сумата, която трябва да се плати за поръчката.
"""


fruit = input()
sets_size = input()
quantity_sets = int(input())

if fruit == 'Watermelon':
    if sets_size == 'small':
        price = (2 * 56) * quantity_sets
    else:
        price = (5 * 28.7) * quantity_sets
elif fruit == 'Mango':
    if sets_size == 'small':
        price = (2 * 36.66) * quantity_sets
    else:
        price = (5 * 19.6) * quantity_sets
elif fruit == 'Pineapple':
    if sets_size == 'small':
        price = (2 * 42.1) * quantity_sets
    else:
        price = (5 * 24.8) * quantity_sets
elif fruit == 'Raspberry':
    if sets_size == 'small':
        price = (2 * 20) * quantity_sets
    else:
        price = (5 * 15.2) * quantity_sets

if 400 <= price <= 1000:
    price = price - price * 0.15
elif price > 1000:
    price = price - price * 0.5
else:
    pass

print(f'{price:.2f} lv.')