"""
Покрай великденските празници, квартален магазин започва да продава боядисани яйца.
Вашата задача е да напишете програма, която да изчислява колко яйца са продадени,
като знаете началната им бройка в магазина. По време на продажбата е възможно да бъдат
доставени допълнителни бройки яйца. Ако в даден момент от изпълнението на програмата,
клиент поиска да купи повече, отколкото има в наличност, или се получи команда "Close",
програмата трябва да приключи изпълнение.
"""

eggs = int(input())
buy = 0

while True:
    line = input()
    if line == 'Close':
        print(f'Store is closed!')
        print(f'{buy} eggs sold.')
        break
    col = int(input())
    if line == 'Fill':
        eggs += col
    else:
        if col > eggs:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {eggs}.')
            break
        buy += col
        eggs -= col


