name = input()

lost_education = 0
total_score = []

while lost_education < 2 and len(total_score) < 12:
    score = float(input())
    if score < 4:
        lost_education += 1
        total_score.append(score)
    else:
        total_score.append(score)


if len(total_score) == 12:
    print(f'{name} graduated. Average grade: {(sum(total_score)/12):.2f}')
else:
    print(f'{name} has been excluded at {len(total_score) - 1} grade')