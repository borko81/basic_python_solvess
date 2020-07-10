from math import floor, ceil


grapes_x = float(input())
grapes_for_one = float(input())
vine_need = float(input())
workers = int(input())

percent_to_work = ((grapes_x * grapes_for_one) * 0.4) / 2.5

diff = percent_to_work - vine_need


if diff < 0:
    print(f'It will be a tough winter! More {floor(abs(diff))} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {floor(percent_to_work)} liters.')
    print(f'{ceil(diff)} liters left -> {ceil(diff / workers)} liters per person.')