"""
Любо очаква гости за Великден. Той разполага с определен бюджет, който е предвидил, за да купи козунаци и боядисани яйца. Известно е, че един козунак стига за трима човека, като всеки гост ще получи и по 2 яйца. Вашата задача е да намерите колко козунака и яйца трябва да купи Любо, както и каква ще е сумата, която той трябва да плати и дали бюджета му е достатъчен. При изчисляването на броя козунаци, които Любо трябва да закупи, техният брой трябва да се закръгли към по-голямото цяло число.  Ако парите не му стигат, трябва да се изведе съобщение, колко не му достигат.
Известно е, че:
    • Един козунак струва 4лв.
    • Едно яйце струва 0.45лв.
"""

from math import ceil

price_cace = 4
price_eggs = 0.45

people = int(input())
budjet = float(input())

needed_cace = ceil(people / 3)
needed_eggs = people * 2

total_price = needed_cace * price_cace + needed_eggs * price_eggs
has_or_not = budjet - total_price

if has_or_not >= 0:
    print(f'Lyubo bought {needed_cace} Easter bread and {needed_eggs} eggs.')
    print(f'He has {has_or_not:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.')
    print(f'He needs {abs(has_or_not):.2f} lv. more.')