import math

couns = 0
change = math.floor(float(input()) * 100)

total = []

while change > 0:
    if change >= 200:
        change -= 200
        total.append(200)
        couns += 1
    elif 100 <= change < 200:
        change -= 100
        total.append(100)
        couns += 1
    elif 50 <= change < 100:
        change -= 50
        total.append(50)
        couns += 1
    elif 20 <= change < 50:
        change -= 20
        total.append(20)
        couns += 1
    elif 10 <= change < 20:
        change -= 10
        total.append(10)
        couns += 1
    elif 5 <= change < 10:
        change -= 5
        total.append(5)
        couns += 1
    elif 2 <= change < 5:
        change -= 2
        total.append(2)
        couns += 1
    elif 1 <= change < 2:
        change -= 1
        total.append(1)
        couns += 1

print(couns)
#print(total)
