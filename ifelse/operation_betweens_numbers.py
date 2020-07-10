N1 = int(input())
N2 = int(input())
operator = input()

if operator == '+':
    result = N1 + N2
    e_o_n = 'even' if result % 2 == 0 else 'odd'
    print(f"{N1} {operator} {N2} = {result} - {e_o_n}")
elif operator == '-':
    result = N1 - N2
    e_o_n = 'even' if result % 2 == 0 else 'odd'
    print(f"{N1} {operator} {N2} = {result} - {e_o_n}")
elif operator == '*':
    result = N1 * N2
    e_o_n = 'even' if result % 2 == 0 else 'odd'
    print(f"{N1} {operator} {N2} = {result} - {e_o_n}")
elif operator == '/':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == '%':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        print(f"{N1} % {N2} = {N1 % N2}")
