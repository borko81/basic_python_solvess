"""
Задача 4. Храна за домашни любимци
Ани има два домашни любимеца - куче и котка. Напишете програма, която изготвя статистика за храната на домашните любимци за определен брой дни. Всеки ден кучето и котката изяждат различно количество от общата им храна. На всеки трети ден получават награда - бисквитки. Количеството на бисквитките е 10% от общо изядената храна за деня.
Вашата програма трябва да отпечатва статистика за количеството бисквитки, които са изяли, колко процента от първоначалното количество обща храна са изяли и колко процента от изядената храна е изяло кучето и котката
"""

days = int(input())
food = float(input())

total_eat = 0
total_cat_eat = 0
total_dog_eat = 0
bisquete_eat = 0

for i in range(1, days + 1):
    dog_eat = float(input())
    cat_eat = float(input())
    e = dog_eat + cat_eat
    total_eat += e
    total_cat_eat += cat_eat
    total_dog_eat += dog_eat

    if i % 3 == 0:
        bisquit = e * 0.1
        bisquete_eat += bisquit


print(f'Total eaten biscuits: {round(bisquete_eat)}gr.')
print(f'{((total_eat / food) * 100):.2f}% of the food has been eaten.')
print(f'{((total_dog_eat / total_eat) * 100):.2f}% eaten from the dog.')
print(f'{((total_cat_eat / total_eat) * 100):.2f}% eaten from the cat.')