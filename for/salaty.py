d = {
    'Facebook': 150,
    'Instagram': 100,
    'Reddit': 50
}

open_tabs = int(input())
salary = int(input())

for i in range(open_tabs):
    name = input()
    salary -= d.get(name, 0)
    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)