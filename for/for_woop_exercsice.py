n = int(input())

sum_even = 0
sum_odd = 0

max_even = -999999
min_even = 999999

max_odd = -999999
min_odd = 999999


for _ in range(1, n+1):
    n = float(input())
    if _ % 2 == 0:
        sum_even += n
        if n > max_even:
            max_even = n
        if n < min_even:
            min_even = n
    else:
        sum_odd += n
        if n > max_odd:
            max_odd = n
        if n < min_odd:
            min_odd = n


if max_even == -999999:
    max_even = 'No'
if min_even == 999999:
    min_even = 'No'
if max_odd == -999999:
    max_odd = 'No'
if min_odd == 999999:
    min_odd = 'No'


print(f'OddSum={sum_odd:.2f},')
try:
    print(f'OddMin={min_odd:.2f},')
except:
    print(f'OddMin=No,')
try:
    print(f'OddMax={max_odd:.2f},')
except:
    print(f'OddMax=No,')
print(f'EvenSum={sum_even:.2f},')
try:
    print(f'EvenMin={min_even:.2f},')
except:
    print(f'EvenMin=No,')
try:
    print(f'EvenMax={max_even:.2f}')
except:
    print(f'EvenMax=No')