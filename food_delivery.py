chicken = int(input())
fish = int(input())
vegan = int(input())

total = chicken * 10.35 + fish * 12.4 + vegan * 8.15
total_with_cace = total + total * 0.2
final_price = total_with_cace + 2.5

print(f'Total: {final_price:.2f}')
