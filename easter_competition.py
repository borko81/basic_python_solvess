"""
С наближаването на Великден, пекарна организира конкурс за направата на най-хубав козунак.
Напишете програма, която да намира сладкаря с най-висок резултат.
В началото на конкурса се въвежда броя на козунаците, които ще бъдат дегустирани от
посетителите на пекарната, като за всеки козунак различен брой посетители, ще дадат оценка
от 1 до 10.

Вход
Първоначално от конзолата се прочита броя на козунаците – цяло число в интервала [1… 100]
След това за всеки козунак се прочита:
    • Името на пекаря, който е направил козунака – текст
    • До получаване на командата "Stop" се прочита
        ◦ оценка за козунак от един човек  – цяло число в интервала [1... 10]
"""

##############11111111111111111################
# counter = int(input())
# data = {}


# while counter > 0:
#     name = input()
#     while True:
#         line = input()
#         if line == 'Stop':
#             print(f'{name} has {data[name]} points.')
#             if data[name] == max(data.values()) and list(data.values()).count(data[name]) == 1:
#                 print(f'{name} is the new number 1!')
#             break
#         score = int(line)
#         if name in data:
#             data[name] += score
#         else:
#             data[name] = score
#     counter -= 1
#
# name, score = sorted(data.items(), key=lambda x: x[1])[-1]
# print(f'{name} won competition with {score} points!')

################22222222222222########################

counter = int(input())
data = {}
winner_name = ''
winner_score = 0

while counter > 0:
    name = input()
    name_score = 0
    while True:
        line = input()
        if line == 'Stop':
            print(f'{name} has {name_score} points.')
            if name_score > winner_score:
                winner_score = name_score
                winner_name = name
                print(f'{name} is the new number 1!')
            break
        score = int(line)
        name_score += score
    counter -= 1

print(f'{winner_name} won competition with {winner_score} points!')