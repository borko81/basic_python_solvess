b = float(input())
c = float(input())
commision = float(input())

b_to_lv = b * 1168

c_to_d = c * 0.15
c_to_lv = c_to_d * 1.76

total_euro = (b_to_lv + c_to_lv) / 1.95

without_comision = total_euro - total_euro * (commision / 100)

print(f'{without_comision:.2f}')