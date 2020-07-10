f_number = int(input())
l_number = int(input())

result = []

for _ in range(f_number, l_number + 1):
    formated_number = list(str(_))
    #print([i for k, i in enumerate(formated_number) if k % 2 == 0])
    odd = [int(i) for k, i in enumerate(formated_number) if k % 2 == 1]
    even = [int(i) for k, i in enumerate(formated_number) if k % 2 == 0]
    if sum(odd) == sum(even):
        result.append(_)

for _ in result:
    print(_, end=' ')