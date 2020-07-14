"""
Напишете програма, която проследява представянето на вашия отбор на благотворителен коледен турнир.  Всеки ден получавате имена на игри до команда "Finish". Със спечелването на всяка една игра печелите по 20лв. за благотворителност. Трябва да изчислите колко пари сте спечелили на края на деня. Ако имате повече спечелени игри, отколкото загубени – вие сте победители този ден и увеличавате парите от него с 10%. При приключване на турнира ако през повечето дни сте били победители печелите турнира и увеличавате всичките спечелени пари с 20%.
Никога няма да имате равен брой спечелени и загубени игри.
"""

days = int(input())

total_win = 0
total_lose = 0
total_money = 0

while days > 0:
    money_win = 0
    save = 0
    not_save = 0

    while True:
        sport = input()
        if sport == 'Finish':
            if save > not_save:
                total_win += 1
                money_win += money_win * 0.1
            else:
                total_lose += 1
            total_money += money_win
            break
        else:
            score = input()
            if score == 'win':
                money_win += 20
                save += 1
            else:
                not_save += 1
    money_win = 0
    save = 0
    not_save = 0
    days -= 1


if total_win > total_lose:
    total_money += total_money * 0.2
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')