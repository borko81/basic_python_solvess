total_standard = 0
total_students = 0
total_kids = 0

while True:
    film = input()
    if film == 'Finish':
        break
    free_space = int(input())
    filled_space = 0
    while filled_space < free_space:
        ticket = input()
        if ticket == 'End':
            break
        else:
            filled_space += 1
            if ticket == "standard":
                total_standard += 1
            elif ticket == "student":
                total_students += 1
            elif ticket == "kid":
                total_kids += 1

    percent_full = filled_space * 100 / free_space
    print(f"{film} - {percent_full:.2f}% full.")


total_tickets = total_students + total_standard + total_kids
percent_students = (total_students / total_tickets) * 100
percent_standard = (total_standard / total_tickets) * 100
percent_kids = (total_kids / total_tickets) * 100


print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")