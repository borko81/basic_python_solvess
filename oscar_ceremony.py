rent = float(input())

statuetki = rent - rent * 0.3
cetering = statuetki - statuetki * 0.15
noise = cetering / 2

total = rent + statuetki + cetering + noise
print(f'{total:.2f}')