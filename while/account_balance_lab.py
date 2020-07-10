total_balance = 0

while total_balance >= 0:
    b = input()
    if b == 'NoMoreMoney':
        break
    else:
        b = float(b)
        if b < 0:
            print('Invalid operation!')
            break
        else:
            total_balance += b
            print(f'Increase: {b:.2f}')


print(f'Total: {total_balance:.2f}')

