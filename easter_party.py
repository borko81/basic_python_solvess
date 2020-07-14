"""
Деси има рожден ден на Великден и иска да организира парти за своите приятели. Тя знае какъв е броят гости, които иска да покани и колко е кувертът за всеки гост. От броя гости зависи и каква отстъпка ще получи за куверта за един човек.
Ако покани:
    • Между 10 (вкл.) и 15 (вкл.) човека -> 15 % отстъпка от куверта за един човек
    • Между 15 и 20 (вкл.) човека -> 20 % отстъпка от куверта за един човек
    • Над 20 човека -> 25 % отстъпка от куверта за един човек
Деси трябва да предвиди и закупуването на торта за партито. Цената на тортата е 10% от бюджета на Деси.
Напишете програма, която изчислява дали бюджетът на Деси ще и е достатъчен за партито.
"""

people = int(input())
price = float(input())
budjet = float(input())

if 10 <= people <= 15:
    price = price - price * 0.15
elif 15 < people <= 20:
    price = price - price * 0.20
elif people > 20:
    price = price - price * 0.25

people_price = people * price
suma_without_cake = (budjet - budjet * 0.1) - people_price

if suma_without_cake >= 0:
    print(f'It is party time! {suma_without_cake:.2f} leva left.')
else:
    print(f'No party! {abs(suma_without_cake):.2f} leva needed.')