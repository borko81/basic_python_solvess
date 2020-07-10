begin_number = int(input())
second_number = int(input())
magic_number = int(input())

counter = 0
solve = False

for x in range(begin_number, second_number + 1):
    for y in range(begin_number, second_number + 1):
        counter += 1
        if x + y == magic_number:
            print(f'Combination N:{counter} ({x} + {y} = {magic_number})')
            solve = True
    if solve == True:
        break


if solve == False:
    print(f'{counter} combinations - neither equals {magic_number}')