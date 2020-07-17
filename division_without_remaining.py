number = int(input())
len_numer = number

result = []

while number > 0:
    line = int(input())
    result.append((line))
    number -= 1

to_two = [i for i in result if i % 2 == 0]
to_three = [i for i in result if i % 3 == 0]
to_four = [i for i in result if i % 4 == 0]


print(f'{((len(to_two) / len_numer) * 100):.2f}%')
print(f'{((len(to_three) / len_numer) * 100):.2f}%')
print(f'{((len(to_four) / len_numer) * 100):.2f}%')