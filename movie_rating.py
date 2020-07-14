counter = int(input())

data = dict()

while counter > 0:
    movie = input()
    rating = float(input())
    data[movie] = rating
    counter -= 1

m = sorted(data.items(), key=lambda x: x[1])
print(f'{m[-1][0]} is with highest rating: {m[-1][1]}')
print(f'{m[0][0]} is with lowest rating: {m[0][1]}')
print(f'Average rating: {(sum(data.values()) / len(data)):.1f}')