from math import ceil, floor

days = int(input())
food_kg = float(input())
food_dog = float(input())
food_cat = float(input())
food_turtle = float(input())

needed_food = days * food_cat + days * food_dog + (days * food_turtle) / 1000

if needed_food > food_kg:
    print(f'{ceil(needed_food - food_kg)} more kilos of food are needed.')
else:
    print(f'{floor(food_kg - needed_food)} kilos of food left.')
