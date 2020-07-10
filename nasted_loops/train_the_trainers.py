juri = int(input())

d = dict()

while True:
    text = input()
    if text == 'Finish':
        break
    else:
        d[text] = []
        for _ in range(juri):
            score = float(input())
            d[text].append(score)


for name, score in d.items():
    s = sum(score) / len(score)
    print(f'{name} - {s:.2f}.')

total_score = sum(list(d.values()), [])

print(f"Student's final assessment is {(sum(total_score) / len(total_score)):.2f}.")