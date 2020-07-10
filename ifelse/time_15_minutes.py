hour = int(input())
minutes = int(input())

minutes += 15

if minutes > 59:
    m = minutes / 60
    h = int(hour + m)
    if h == 24:
        h = 0
    time = f'{h}:{str(minutes%60).zfill(2)}'
else:
    time = f'{hour}:{minutes}'

print(time)