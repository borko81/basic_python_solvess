simple = input()
town = input()
quantity = float(input())

if town == 'Sofia':
    if simple == 'coffee':
        print(f'{0.5 * quantity:.2f}')
    elif simple == 'water':
        print(f'{0.80 * quantity:.2f}')
    elif simple == 'beer':
        print(f'{1.2 * quantity:.2f}')
    elif simple == 'sweets':
        print(f'{1.45 * quantity:.2f}')
    elif simple == 'peanuts':
        print(f'{1.60 * quantity:.2f}')
elif town == 'Plovdiv':
    if simple == 'coffee':
        print(f'{0.40 * quantity:.2f}')
    elif simple == 'water':
        print(f'{0.70 * quantity:.2f}')
    elif simple == 'beer':
        print(f'{1.15 * quantity:.2f}')
    elif simple == 'sweets':
        print(f'{1.30 * quantity:.2f}')
    elif simple == 'peanuts':
        print(f'{1.50 * quantity:.2f}')
elif town == 'Varna':
    if simple == 'coffee':
        print(f'{0.45 * quantity:.2f}')
    elif simple == 'water':
        print(f'{0.70 * quantity:.2f}')
    elif simple == 'beer':
        print(f'{1.10 * quantity:.2f}')
    elif simple == 'sweets':
        print(f'{1.35 * quantity:.2f}')
    elif simple == 'peanuts':
        print(print(f'{1.55 * quantity:.2f}'))