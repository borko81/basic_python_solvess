from math import floor

need_work = float(input())
days = int(input())
overtime_employe = int(input())

hours_to_work = (days - days * 0.1) * 8
hours_overtime = (overtime_employe * 2) * days

sum_work_hours = floor(hours_overtime + hours_to_work)


if sum_work_hours >= need_work:
    print(f'Yes!{floor(sum_work_hours - need_work)} hours left.')
else:
    print(f'Not enough time!{floor(need_work-sum_work_hours)} hours needed.')