vaucher = float(input())

order = input()
total_sum = 0
ticket = 0
product = 0

while order != 'End':
    if len(order) > 8:
        s = sum([ord(i) for i in order[:2]])
        if s > vaucher:
            break
        vaucher -= s
        ticket += 1
    else:
        s = sum([ord(i) for i in order[:1]])
        if s > vaucher:
            break
        vaucher -= s
        product += 1
    order = input()

# Result
print(ticket)
print(product)