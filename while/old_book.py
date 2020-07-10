book_search = input()

count = 0
found = False
book = input()

while book != 'No More Books':
    if book_search == book:
        found = True
        break
    count += 1
    book = input()


if found == False:
    print('The book you search is not here!')
    print(f'You checked {count} books.')
else:
    print(f"You checked {count} books and found it.")