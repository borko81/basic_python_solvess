cake_h = int(input())
cake_w = int(input())

size = cake_h * cake_w

while size >= 0:
    piece = input()
    if piece == 'STOP':
        break
    else:
        size -= int(piece)

if size < 0:
    print(f'No more cake left! You need {abs(size)} pieces more.')
else:
    print(f'{size} pieces are left.')