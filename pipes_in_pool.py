v = float(input())
p1 = float(input())
p2 = float(input())
h = float(input())

p1_fuew = h * p1
p2_fuew = h * p2

total_fuel = p1_fuew + p2_fuew

if v < total_fuel:
    diff = total_fuel - v
    print(f'For {h} hours the pool overflows with {diff} liters.')
else:
    percent_fuel = (total_fuel / v) * 100
    p1_percent = (p1_fuew / total_fuel) * 100
    p2_percent = (p2_fuew / total_fuel) * 100
    print(f'The pool is {percent_fuel:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.')