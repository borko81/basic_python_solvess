"""
Предстои Великден и едно от най-вълнуващите неща е боядисването на яйца.
Наличните цветове за боядисване са:
    • червено (red)
    • оранжев (orange)
    • син (blue)
    • зелен (green)
Напишете програма, която изчислява какъв е броят на яйцата от всеки цвят
и от кой цвят яйцата са най - много, като знаете общия им брой и цвета на всяко яйце.
"""

collored_egs = int(input())

data = {'red': 0, 'blue': 0, 'green': 0, 'orange': 0}


while collored_egs > 0:
    color = input()
    if color == 'red':
        data['red'] += 1
    elif color == 'blue':
        data['blue'] += 1
    elif color == 'green':
        data['green'] += 1
    else:
        data['orange'] += 1
    collored_egs -= 1


print(f'Red eggs: {data["red"]}')
print(f'Orange eggs: {data["orange"]}')
print(f'Blue eggs: {data["blue"]}')
print(f'Green eggs: {data["green"]}')

color, m_egs = sorted(data.items(), key=lambda x: x[1])[-1]
print(f'Max eggs: {m_egs} -> {color}')


