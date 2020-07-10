x = float(input())
y = float(input())
h = float(input())

# kwadrat = x * x
# pravoagalnik = x * y
# triagalnik = (x * h) / 2

two_wall = x * y
windwos = 1.5 * 1.5

back_front_wall = x * x
entry = 1.2 * 2

roof_triangel = ((x * h) / 2) * 2
roof_rectangle = ((x * y) * 2)

total_wall = 2 * two_wall - 2 * windwos
total_back_and_front = 2 * back_front_wall - entry

green_color = (total_wall + total_back_and_front) / 3.4
red_color = (roof_rectangle + roof_triangel) / 4.3

print(f'{green_color:.2f}')
print(f'{red_color:.2f}')




