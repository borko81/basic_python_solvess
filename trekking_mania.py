"""
Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата, катерачите ще изкачват различни върхове.
    • Група до 5 човека– Мусала
    • Група от 6 до 12 – Монблан
    • Група от 13 до 25 – Килиманджаро
    • Група от 26 до 40 – К2
    • Група от 41 или повече – Еверест
Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
"""

count_group = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

while count_group > 0:
    people = int(input())
    if 1 <= people <= 5:
        musala += people
    elif 5 < people <= 12:
        monblan += people
    elif 12 < people <= 25:
        kilimandjaro += people
    elif 25 < people <= 40:
        k2 += people
    else:
        everest += people
    count_group -= 1

total_people = musala + monblan + kilimandjaro + k2 + everest

print(f'{((musala / total_people) * 100):.2f}%')
print(f'{((monblan / total_people) * 100):.2f}%')
print(f'{((kilimandjaro / total_people) * 100):.2f}%')
print(f'{((k2 / total_people) * 100):.2f}%')
print(f'{((everest / total_people) * 100):.2f}%')