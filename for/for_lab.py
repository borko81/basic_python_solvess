# number = int(input())
#
# for i in range(number+1):
#     if i % 2 == 0:
#         print(2 ** i)
# ======================================
# words = input()
# total = 0
#
# for _ in words:
#     if _ == 'a':
#         total += 1
#     elif _ == 'e':
#         total += 2
#     elif _ == 'i':
#         total += 3
#     elif _ == 'o':
#         total += 4
#     elif _ == 'u':
#         total += 5
#
# print(total)
# ======================================

# number = int(input())
# total = 0
#
# for _ in range(number):
#     total += int(input())
#
# print(total)
# ======================================

# number = int(input())
# result = []
#
# for _ in range(number):
#     result.append(int(input()))
#
#
# print(f'Max number: {max(result)}')
# print(f'Min number: {min(result)}')

# ======================================

# number = int(input())
#
# result = []
#
# for _ in range(number*2):
#     result.append(int(input()))
#
#
# if sum(result[0:number]) == sum(result[number:]):
#     print(f'Yes, sum = {sum(result[0:number])}')
# else:
#     print(f'No, diff = {abs(sum(result[0:number]) - sum(result[number:]) )}')

# ======================================

# number = int(input())
#
# odd = []
# even = []
#
# for _ in range(number):
#     if _ % 2 == 0:
#         even.append((int(input())))
#     else:
#         odd.append((int(input())))
#
# if sum(odd) == sum(even):
#     print('Yes')
#     print(f'Sum = {sum(odd)}')
# else:
#     print('No')
#     print(f'Diff = {abs(sum(odd) - sum(even))}')

# ======================================

years = int(input())
cost = float(input())
toys_price = int(input())

sum_toys = 0
cash = 0

for _ in range(1, years+1):
    if _%2 ==1 :
        sum_toys += 1
    if _%2 == 0:
        cash += 1

totaly_toys = sum_toys * toys_price
totalt_cash = sum([i * 10 for i in range(1, cash + 1)])

total_sum = (totalt_cash + totaly_toys) - cash * 1

left = total_sum - cost

if left >= 0:
    print(f"Yes! {left:.2f}")
else:
    print(f'No! {(cost - total_sum):.2f}')




























