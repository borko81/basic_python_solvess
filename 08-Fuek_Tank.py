fuel_choice = input()
l = float(input())

if fuel_choice not in ["Diesel", "Gasoline","Gas"]:
    print(f'Invalid fuel!')
else:
    if l >= 25:
        print(f'You have enough {fuel_choice.lower()}.')
    elif l < 25:
        print(f'Fill your tank with {fuel_choice.lower()}!')