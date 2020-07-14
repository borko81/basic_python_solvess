movie_name = input()

student = 0
standard = 0
kid = 0

while movie_name != 'Finish':

    free_ceats = int(input())
    get_ceats = free_ceats
    counter_movie_seats = 0

    while free_ceats > 0:
        order = input()

        if order == 'End':
            break
        elif order == 'student':
            student += 1
        elif order == 'standard':
            standard += 1
        elif order == 'kid':
            kid += 1

        free_ceats -= 1
        counter_movie_seats += 1

    print(f'{movie_name} - {(( counter_movie_seats / get_ceats ) * 100):.2f}% full.')
    movie_name = input()


total_buy_tickets = standard + student + kid

print(f'Total tickets: {total_buy_tickets}')
print(f'{((student / total_buy_tickets) * 100):.2f}% student tickets.')
print(f'{((standard / total_buy_tickets) * 100):.2f}% standard tickets.')
print(f'{((kid / total_buy_tickets) * 100):.2f}% kids tickets.')