fruit = input()
days = input()
quantity = float(input())

data = {
    'banana': [2.50, 2.70],
    'apple': [1.20, 1.250],
    'orange': [0.85, 0.90],
    'grapefruit': [1.45, 1.60],
    'kiwi': [2.70, 3.00],
    'pineapple': [5.50, 5.60],
    'grapes': [3.85, 4.20]
}

f = 'banana apple orange grapefruit kiwi pineapple grapes'.split(' ')

if days in ['Saturday', 'Sunday'] and fruit in f:
    print(f'{(quantity * data[fruit][1]):.2f}')
elif days in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] and fruit in f:
    print(f'{(quantity * data[fruit][0]):.2f}')
else:
    print('error')