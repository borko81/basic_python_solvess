hollidays = int(input())
year = 365
work_days = year - hollidays
total_time = 30000


total_play_time = hollidays * 127 + work_days * 63

diff = total_time - total_play_time

if diff < 0:
    M = abs(diff) % 60
    H = abs(diff) // 60
    print(f'Tom will run away')
    print(f'{H} hours and {M} minutes more for play')
else:
    M = abs(diff) % 60
    H = abs(diff) // 60
    print('Tom sleeps well')
    print(f'{H} hours and {M} minutes less for play')