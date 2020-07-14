"""
На Великден семейството на Деси се събира и тя решава да организира "битка" между великденски яйца.
Правилата на "битката" са следните:
    • Участват двама играчи
    • Всеки от тях започва с определен брой яйца
    • При получаване на команда "one" -> първият играч печели => яйцата на втория намаляват с едно
    • При получаване на команда "two" -> вторият играч печели => яйцата на първия намаляват с едно
    • Играта приключва, ако някой от играчите остане без яйца или до получаване на команда "End of battle"
"""

f_eggs = int(input())
s_eggs = int(input())

while True:
    line = input()
    if line == 'End of battle':
        print(f'Player one has {f_eggs} eggs left.')
        print(f'Player two has {s_eggs} eggs left.')
        break
    if line == 'one':
        s_eggs -= 1
    elif line == 'two':
        f_eggs -= 1
    if f_eggs <= 0:
        print(f'Player one is out of eggs. Player two has {s_eggs} eggs left.')
        break
    elif s_eggs <= 0:
        print(f'Player two is out of eggs. Player one has {f_eggs} eggs left.')
        break