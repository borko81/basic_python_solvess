"""
Предстои Великден и Деси е решила да изпече домашни
козунаци за колегите си. Главните продукти, които ще трябват на Деси са:
брашно и захар. Един пакет захар е 950 грама, а един пакет брашно е 750 грама.
Напишете програма, която изчислява колко пакета захар и брашно трябва да купи Деси,
за да й стигнат за направата на козунаците, като знаете за всеки един козунак по колко
грама захар и брашно са изразходени. Също намерете кое е най-голямото количество
захар и брашно, които са използвани.
"""

from math import ceil

count = int(input())

sugar = []
brashno = []

while count > 0:
    s = int(input())
    sugar.append(s)
    b = int(input())
    brashno.append(b)
    count -= 1

packet_sugar = ceil(sum(sugar) / 950)
packet_brashno = ceil(sum(brashno) / 750)

print(f'Sugar: {packet_sugar}')
print(f'Flour: {packet_brashno}')
print(f'Max used flour is {max(brashno)} grams, max used sugar is {max(sugar)} grams.')