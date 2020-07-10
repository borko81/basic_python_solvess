days = int(input())
room = input()
evaluation = input()

nights = days - 1

if room == 'room for one person' and nights < 10:
    price = nights * 18.00
elif room == 'room for one person' and 10 <= nights <= 15:
    price = nights * 18.00
elif room == 'room for one person' and nights > 15:
    price = nights * 18.00

if room == 'apartment' and nights < 10:
    price = nights * 25.00
    price = price - (price * 0.3)
elif room == 'apartment' and 10 <= nights <= 15:
    price = nights * 25.00
    price = price - (price * 0.35)
elif room == 'apartment' and nights > 15:
    price = nights * 25.00
    price = price - (price * 0.5)

if room == 'president apartment' and nights < 10:
    price = nights * 35.00
    price = price - (price * 0.1)
elif room == 'president apartment' and 10 <= nights <= 15:
    price = nights * 35.00
    price = price - (price * 0.15)
elif room == 'president apartment' and nights > 15:
    price = nights * 35.00
    price = price - (price * 0.2)

if evaluation == 'positive':
    price = price + (price * 0.25)
else:
    price = price - (price * 0.10)

print(f'{price:.2f}')