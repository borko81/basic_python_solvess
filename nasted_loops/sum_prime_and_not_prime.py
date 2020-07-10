prime = 0
not_prime = 0

while True:
    number = input()
    if number == 'stop':
        break
    else:
        p = True
        number = int(number)
        if number < 0:
            print('Number is negative.')
        else:
            for _ in range(2, (number // 2) + 1):
                if number % _ == 0:
                    p = False
                    break
            if p == False:
                not_prime += number
            else:
                prime += number


print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {not_prime}')