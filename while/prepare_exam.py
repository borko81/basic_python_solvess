count_not_enought = int(input())

exam = []
not_enought = 0
last_test = ''
grade = 0

while True:
    text = input()
    if text == 'Enough':
        break
    evaluation = int(input())
    if evaluation <= 4:
        not_enought += 1
    if not_enought == count_not_enought:
        break
    grade += evaluation
    exam.append(text)


if not_enought < count_not_enought:
    print(f'Average score: {(grade/ len(exam)):.2f}')
    print(f'Number of problems: {len(exam)}')
    print(f'Last problem: {exam[-1]}')
else:
    print(f'You need a break, {count_not_enought} poor grades.')