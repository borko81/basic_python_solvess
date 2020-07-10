needed_money = float(input())
owned_money = float(input())

count_days = 0
spend_days = 0


while owned_money < needed_money and spend_days < 5:
    action = input()
    count_days += 1
    if action.lower() == 'spend':
        spend_days += 1
        money = float(input())
        if money >= owned_money:
            owned_money = 0
        else:
            owned_money -= money
    if action.lower() == 'save':
        spend_days = 0
        money = float(input())
        owned_money += money


if owned_money >= needed_money:
    print(f'You saved the money for {count_days} days.')

if spend_days == 5:
    print(f"You can't save the money.")
    print(f'{count_days}')