bottle = int(input())
count = 0

quality_len = bottle * 750
plate_clean = 0
tava_clean = 0


while quality_len >= 0:
    dishes = input()
    if dishes == 'End':
        break
    else:
        count += 1
        washes = int(dishes)
        if count % 3 != 0:
            plate_clean += washes
            lost_preparat = washes * 5
            quality_len -= lost_preparat
        else:
            lost_preparat = washes * 15
            tava_clean += washes
            quality_len -= lost_preparat


if quality_len < 0:
    print(f'Not enough detergent, {abs(quality_len)} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{plate_clean} dishes and {tava_clean} pots were washed.')
    print(f'Leftover detergent {quality_len} ml.')