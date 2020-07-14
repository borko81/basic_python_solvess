"""
Георги решава да подобри рекорда за най-бързо изкачване на връх Монблан. На конзолата се въвежда рекордът в секунди, който Георги трябва да подобри, разстоянието в метри, което трябва да изкачи и времето в секунди, за което той изкачва 1 метър. Да се напише програма, която изчислява дали се е справил със задачата, като се има предвид, че: наклона на терена го забавя на всеки 50 м. с 30 секунди. Да се изчисли времето в секунди, за което Георги ще изкачи разстоянието до върха и разликата спрямо рекорда.
Когато се изчислява колко пъти Георги ще се забави в резултат на наклона на терена, резултатът трябва да се закръгли надолу до най-близкото цяло число.
"""

from math import floor

recors = float(input())
distance = float(input())
time_for_one_meters = float(input())

lose_time = floor(distance / 50) * 30

get_time_for_distance = (distance * time_for_one_meters) + lose_time

if get_time_for_distance >= recors:
    print(f'No! He was {(get_time_for_distance - recors):.2f} seconds slower.')
else:
    print(f'Yes! The new record is {(get_time_for_distance):.2f} seconds.')

