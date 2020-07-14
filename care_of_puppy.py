food_by = int(input())
food_by_to_gt = food_by * 1000

while True:
    eat = input()
    if eat == 'Adopted':
        break
    else:
        food_by_to_gt -= int(eat)

if food_by_to_gt >= 0:
    print(f'Food is enough! Leftovers: {food_by_to_gt} grams.')
else:
    print(f'Food is not enough. You need {abs(food_by_to_gt)} grams more.')