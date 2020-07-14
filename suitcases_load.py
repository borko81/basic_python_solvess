"""
Напишете програма, която ви помага при товаренето на куфари в багажника на самолет. Всеки самолет има определен капацитет на багажника. До получаване на команда "End" ще получавате обем на куфар. Обемът на всеки трети куфар трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане. Ако свободното пространството в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.
"""

capacity = float(input())
suitcase_total = 0

v = 0

while True:
    v += 1
    line = input()
    if line == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        break
    else:
        size = float(line)
        if v % 3 == 0:
            size = size + size * 0.1
        if size > capacity:
            print(f'No more space!')
            break
        suitcase_total += 1
        capacity -= size


print(f'Statistic: {suitcase_total} suitcases loaded.')