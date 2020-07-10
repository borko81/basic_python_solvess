w = int(input())
l = int(input())
h = int(input())

check = w * l * h

while True:
    box = input()
    if box == 'Done':
        print(f'{check} Cubic meters left.')
        break
    else:
        check -= int(box)
        if check < 0:
            print(f'No more free space! You need {abs(check)} Cubic meters more.')
            break
