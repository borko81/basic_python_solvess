
while True:
    destination = input()
    if destination == 'End':
        break
    else:
        min_money = float(input())
        while min_money > 0:
            spend_money = float(input())
            min_money -= spend_money
        print(f'Going to {destination}!')