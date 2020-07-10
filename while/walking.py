goal = 10000

total_steps = 0

while True:
    step = input()
    if step == 'Going home':
        step = int(input())
        total_steps += step
        break
    else:
        total_steps += int(step)
    if total_steps >= goal:
        break


if total_steps >= goal:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")
else:
    print(f'{goal - total_steps} more steps to reach goal.')